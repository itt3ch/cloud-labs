from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import screen_size_controller
from my_project.auth.domain.orders.ScreenSize import ScreenSize

screen_size_bp = Blueprint('screen_size', __name__, url_prefix='/screen-size')

@screen_size_bp.get('')
def get_all_screen_sizes() -> Response:
    sizes = screen_size_controller.find_all()
    sizes_dto = [size.put_into_dto() for size in sizes]
    return make_response(jsonify(sizes_dto), HTTPStatus.OK)

@screen_size_bp.post('')
def create_screen_size() -> Response:
    content = request.get_json()
    size = ScreenSize.create_from_dto(content)
    screen_size_controller.create(size)
    return make_response(jsonify(size.put_into_dto()), HTTPStatus.CREATED)

@screen_size_bp.get('/<int:size_id>')
def get_screen_size(size_id: int) -> Response:
    size = screen_size_controller.find_by_id(size_id)
    if size:
        return make_response(jsonify(size.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Screen size not found"}), HTTPStatus.NOT_FOUND)

@screen_size_bp.put('/<int:size_id>')
def update_screen_size(size_id: int) -> Response:
    content = request.get_json()
    size = ScreenSize.create_from_dto(content)
    screen_size_controller.update(size_id, size)
    return make_response("Screen size updated", HTTPStatus.OK)

@screen_size_bp.delete('/<int:size_id>')
def delete_screen_size(size_id: int) -> Response:
    screen_size_controller.delete(size_id)
    return make_response("Screen size deleted", HTTPStatus.NO_CONTENT)
