from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import resolution_controller
from my_project.auth.domain.orders.Resolution import Resolution

resolution_bp = Blueprint('resolution', __name__, url_prefix='/resolution')

@resolution_bp.get('')
def get_all_resolutions() -> Response:
    resolutions = resolution_controller.find_all()
    resolutions_dto = [resolution.put_into_dto() for resolution in resolutions]
    return make_response(jsonify(resolutions_dto), HTTPStatus.OK)

@resolution_bp.post('')
def create_resolution() -> Response:
    content = request.get_json()
    resolution = Resolution.create_from_dto(content)
    resolution_controller.create(resolution)
    return make_response(jsonify(resolution.put_into_dto()), HTTPStatus.CREATED)

@resolution_bp.get('/<int:resolution_id>')
def get_resolution(resolution_id: int) -> Response:
    resolution = resolution_controller.find_by_id(resolution_id)
    if resolution:
        return make_response(jsonify(resolution.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Resolution not found"}), HTTPStatus.NOT_FOUND)

@resolution_bp.put('/<int:resolution_id>')
def update_resolution(resolution_id: int) -> Response:
    content = request.get_json()
    resolution = Resolution.create_from_dto(content)
    resolution_controller.update(resolution_id, resolution)
    return make_response("Resolution updated", HTTPStatus.OK)

@resolution_bp.delete('/<int:resolution_id>')
def delete_resolution(resolution_id: int) -> Response:
    resolution_controller.delete(resolution_id)
    return make_response("Resolution deleted", HTTPStatus.NO_CONTENT)
