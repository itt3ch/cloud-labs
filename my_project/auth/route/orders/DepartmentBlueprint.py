from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import department_controller
from my_project.auth.domain.orders.Department import Department

department_bp = Blueprint('department', __name__, url_prefix='/department')

@department_bp.get('')
def get_all_departments() -> Response:
    departments = department_controller.find_all()
    departments_dto = [dept.put_into_dto() for dept in departments]
    return make_response(jsonify(departments_dto), HTTPStatus.OK)

@department_bp.post('')
def create_department() -> Response:
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.create(department)
    return make_response(jsonify(department.put_into_dto()), HTTPStatus.CREATED)

@department_bp.get('/<int:department_id>')
def get_department(department_id: int) -> Response:
    dept = department_controller.find_by_id(department_id)
    if dept:
        return make_response(jsonify(dept.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Department not found"}), HTTPStatus.NOT_FOUND)

@department_bp.put('/<int:department_id>')
def update_department(department_id: int) -> Response:
    content = request.get_json()
    department = Department.create_from_dto(content)
    department_controller.update(department_id, department)
    return make_response("Department updated", HTTPStatus.OK)

@department_bp.delete('/<int:department_id>')
def delete_department(department_id: int) -> Response:
    department_controller.delete(department_id)
    return make_response("Department deleted", HTTPStatus.NO_CONTENT)
