from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import panel_manufacturer_controller
from my_project.auth.domain.orders.PanelManufacturer import PanelManufacturer

panel_manufacturer_bp = Blueprint('panel_manufacturer', __name__, url_prefix='/panel-manufacturer')

@panel_manufacturer_bp.get('')
def get_all_panel_manufacturers() -> Response:
    manufacturers = panel_manufacturer_controller.find_all()
    manufacturers_dto = [manufacturer.put_into_dto() for manufacturer in manufacturers]
    return make_response(jsonify(manufacturers_dto), HTTPStatus.OK)

@panel_manufacturer_bp.post('')
def create_panel_manufacturer() -> Response:
    content = request.get_json()
    manufacturer = PanelManufacturer.create_from_dto(content)
    panel_manufacturer_controller.create(manufacturer)
    return make_response(jsonify(manufacturer.put_into_dto()), HTTPStatus.CREATED)

@panel_manufacturer_bp.get('/<int:manufacturer_id>')
def get_panel_manufacturer(manufacturer_id: int) -> Response:
    manufacturer = panel_manufacturer_controller.find_by_id(manufacturer_id)
    if manufacturer:
        return make_response(jsonify(manufacturer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Manufacturer not found"}), HTTPStatus.NOT_FOUND)

@panel_manufacturer_bp.put('/<int:manufacturer_id>')
def update_panel_manufacturer(manufacturer_id: int) -> Response:
    content = request.get_json()
    manufacturer = PanelManufacturer.create_from_dto(content)
    panel_manufacturer_controller.update(manufacturer_id, manufacturer)
    return make_response("Manufacturer updated", HTTPStatus.OK)

@panel_manufacturer_bp.delete('/<int:manufacturer_id>')
def delete_panel_manufacturer(manufacturer_id: int) -> Response:
    panel_manufacturer_controller.delete(manufacturer_id)
    return make_response("Manufacturer deleted", HTTPStatus.NO_CONTENT)
