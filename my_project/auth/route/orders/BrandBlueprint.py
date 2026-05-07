from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import brand_controller
from my_project.auth.domain.orders.Brand import Brand

brand_bp = Blueprint('brand', __name__, url_prefix='/brand')

@brand_bp.get('')
def get_all_brands() -> Response:
    brands = brand_controller.find_all()
    brands_dto = [brand.put_into_dto() for brand in brands]
    return make_response(jsonify(brands_dto), HTTPStatus.OK)

@brand_bp.post('')
def create_brand() -> Response:
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.create(brand)
    return make_response(jsonify(brand.put_into_dto()), HTTPStatus.CREATED)

@brand_bp.get('/<int:brand_id>')
def get_brand(brand_id: int) -> Response:
    brand = brand_controller.find_by_id(brand_id)
    if brand:
        return make_response(jsonify(brand.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Brand not found"}), HTTPStatus.NOT_FOUND)

@brand_bp.put('/<int:brand_id>')
def update_brand(brand_id: int) -> Response:
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.update(brand_id, brand)
    return make_response("Brand updated", HTTPStatus.OK)

@brand_bp.delete('/<int:brand_id>')
def delete_brand(brand_id: int) -> Response:
    brand_controller.delete(brand_id)
    return make_response("Brand deleted", HTTPStatus.NO_CONTENT)
