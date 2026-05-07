from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import supermarket_controller
from my_project.auth.domain.orders.Supermarket import Supermarket

supermarket_bp = Blueprint('supermarket', __name__, url_prefix='/supermarket')

@supermarket_bp.get('')
def get_all_supermarkets() -> Response:
    supermarkets = supermarket_controller.find_all()
    supermarkets_dto = [market.put_into_dto() for market in supermarkets]
    return make_response(jsonify(supermarkets_dto), HTTPStatus.OK)

@supermarket_bp.post('')
def create_supermarket() -> Response:
    content = request.get_json()
    supermarket = Supermarket.create_from_dto(content)
    supermarket_controller.create(supermarket)
    return make_response(jsonify(supermarket.put_into_dto()), HTTPStatus.CREATED)

@supermarket_bp.get('/<int:supermarket_id>')
def get_supermarket(supermarket_id: int) -> Response:
    market = supermarket_controller.find_by_id(supermarket_id)
    if market:
        return make_response(jsonify(market.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Supermarket not found"}), HTTPStatus.NOT_FOUND)

@supermarket_bp.put('/<int:supermarket_id>')
def update_supermarket(supermarket_id: int) -> Response:
    content = request.get_json()
    supermarket = Supermarket.create_from_dto(content)
    supermarket_controller.update(supermarket_id, supermarket)
    return make_response("Supermarket updated", HTTPStatus.OK)

@supermarket_bp.delete('/<int:supermarket_id>')
def delete_supermarket(supermarket_id: int) -> Response:
    supermarket_controller.delete(supermarket_id)
    return make_response("Supermarket deleted", HTTPStatus.NO_CONTENT)
