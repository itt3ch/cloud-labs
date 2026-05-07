from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import refresh_rate_controller
from my_project.auth.domain.orders.RefreshRate import RefreshRate

refresh_rate_bp = Blueprint('refresh_rate', __name__, url_prefix='/refresh-rate')

@refresh_rate_bp.get('')
def get_all_refresh_rates() -> Response:
    refresh_rates = refresh_rate_controller.find_all()
    refresh_rates_dto = [rate.put_into_dto() for rate in refresh_rates]
    return make_response(jsonify(refresh_rates_dto), HTTPStatus.OK)

@refresh_rate_bp.post('')
def create_refresh_rate() -> Response:
    content = request.get_json()
    rate = RefreshRate.create_from_dto(content)
    refresh_rate_controller.create(rate)
    return make_response(jsonify(rate.put_into_dto()), HTTPStatus.CREATED)

@refresh_rate_bp.get('/<int:rate_id>')
def get_refresh_rate(rate_id: int) -> Response:
    rate = refresh_rate_controller.find_by_id(rate_id)
    if rate:
        return make_response(jsonify(rate.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Refresh rate not found"}), HTTPStatus.NOT_FOUND)

@refresh_rate_bp.put('/<int:rate_id>')
def update_refresh_rate(rate_id: int) -> Response:
    content = request.get_json()
    rate = RefreshRate.create_from_dto(content)
    refresh_rate_controller.update(rate_id, rate)
    return make_response("Refresh rate updated", HTTPStatus.OK)

@refresh_rate_bp.delete('/<int:rate_id>')
def delete_refresh_rate(rate_id: int) -> Response:
    refresh_rate_controller.delete(rate_id)
    return make_response("Refresh rate deleted", HTTPStatus.NO_CONTENT)
