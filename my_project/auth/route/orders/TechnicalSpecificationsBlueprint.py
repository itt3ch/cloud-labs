from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import technical_specifications_controller
from my_project.auth.domain.orders.TechnicalSpecifications import TechnicalSpecifications

technical_specifications_bp = Blueprint('technical_specifications', __name__, url_prefix='/technical-specifications')

@technical_specifications_bp.get('')
def get_all_technical_specifications() -> Response:
    specs = technical_specifications_controller.find_all()
    specs_dto = [spec.put_into_dto() for spec in specs]
    return make_response(jsonify(specs_dto), HTTPStatus.OK)

@technical_specifications_bp.post('')
def create_technical_specifications() -> Response:
    content = request.get_json()
    spec = TechnicalSpecifications.create_from_dto(content)
    technical_specifications_controller.create(spec)
    return make_response(jsonify(spec.put_into_dto()), HTTPStatus.CREATED)

@technical_specifications_bp.get('/<int:spec_id>')
def get_technical_specifications(spec_id: int) -> Response:
    spec = technical_specifications_controller.find_by_id(spec_id)
    if spec:
        return make_response(jsonify(spec.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Technical specification not found"}), HTTPStatus.NOT_FOUND)

@technical_specifications_bp.put('/<int:spec_id>')
def update_technical_specifications(spec_id: int) -> Response:
    content = request.get_json()
    spec = TechnicalSpecifications.create_from_dto(content)
    technical_specifications_controller.update(spec_id, spec)
    return make_response("Technical specifications updated", HTTPStatus.OK)

@technical_specifications_bp.delete('/<int:spec_id>')
def delete_technical_specifications(spec_id: int) -> Response:
    technical_specifications_controller.delete(spec_id)
    return make_response("Technical specifications deleted", HTTPStatus.NO_CONTENT)
