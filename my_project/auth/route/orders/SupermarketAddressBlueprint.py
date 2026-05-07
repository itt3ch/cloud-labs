from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import supermarket_address_controller
from my_project.auth.domain.orders.SupermarketAddress import SupermarketAddress

supermarket_address_bp = Blueprint('supermarket_address', __name__, url_prefix='/supermarket-address')

@supermarket_address_bp.get('')
def get_all_addresses() -> Response:
    addresses = supermarket_address_controller.find_all()
    addresses_dto = [address.put_into_dto() for address in addresses]
    return make_response(jsonify(addresses_dto), HTTPStatus.OK)

@supermarket_address_bp.post('')
def create_address() -> Response:
    content = request.get_json()
    address = SupermarketAddress.create_from_dto(content)
    supermarket_address_controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)

@supermarket_address_bp.get('/<int:address_id>')
def get_address(address_id: int) -> Response:
    address = supermarket_address_controller.find_by_id(address_id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Address not found"}), HTTPStatus.NOT_FOUND)

@supermarket_address_bp.put('/<int:address_id>')
def update_address(address_id: int) -> Response:
    content = request.get_json()
    address = SupermarketAddress.create_from_dto(content)
    supermarket_address_controller.update(address_id, address)
    return make_response("Address updated", HTTPStatus.OK)

@supermarket_address_bp.delete('/<int:address_id>')
def delete_address(address_id: int) -> Response:
    supermarket_address_controller.delete(address_id)
    return make_response("Address deleted", HTTPStatus.NO_CONTENT)
