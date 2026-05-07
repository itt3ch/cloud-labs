from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import panel_controller
from my_project.auth.domain.orders.Panel import Panel

panel_bp = Blueprint('panel', __name__, url_prefix='/panel')

@panel_bp.get('')
def get_all_panels() -> Response:
    panels = panel_controller.find_all()
    panels_dto = [panel.put_into_dto() for panel in panels]
    return make_response(jsonify(panels_dto), HTTPStatus.OK)

@panel_bp.post('')
def create_panel() -> Response:
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    panel_controller.create(panel)
    return make_response(jsonify(panel.put_into_dto()), HTTPStatus.CREATED)

@panel_bp.get('/<int:panel_id>')
def get_panel(panel_id: int) -> Response:
    panel = panel_controller.find_by_id(panel_id)
    if panel:
        return make_response(jsonify(panel.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Panel not found"}), HTTPStatus.NOT_FOUND)

@panel_bp.put('/<int:panel_id>')
def update_panel(panel_id: int) -> Response:
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    panel_controller.update(panel_id, panel)
    return make_response("Panel updated", HTTPStatus.OK)

@panel_bp.delete('/<int:panel_id>')
def delete_panel(panel_id: int) -> Response:
    panel_controller.delete(panel_id)
    return make_response("Panel deleted", HTTPStatus.NO_CONTENT)
