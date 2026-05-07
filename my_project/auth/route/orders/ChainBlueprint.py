from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import chain_controller
from my_project.auth.domain.orders.Chain import Chain

chain_bp = Blueprint('chain', __name__, url_prefix='/chain')

@chain_bp.get('')
def get_all_chains() -> Response:
    chains = chain_controller.find_all()
    chains_dto = [chain.put_into_dto() for chain in chains]
    return make_response(jsonify(chains_dto), HTTPStatus.OK)

@chain_bp.post('')
def create_chain() -> Response:
    content = request.get_json()
    chain = Chain.create_from_dto(content)
    chain_controller.create(chain)
    return make_response(jsonify(chain.put_into_dto()), HTTPStatus.CREATED)

@chain_bp.get('/<int:chain_id>')
def get_chain(chain_id: int) -> Response:
    chain = chain_controller.find_by_id(chain_id)
    if chain:
        return make_response(jsonify(chain.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Chain not found"}), HTTPStatus.NOT_FOUND)

@chain_bp.put('/<int:chain_id>')
def update_chain(chain_id: int) -> Response:
    content = request.get_json()
    chain = Chain.create_from_dto(content)
    chain_controller.update(chain_id, chain)
    return make_response("Chain updated", HTTPStatus.OK)

@chain_bp.delete('/<int:chain_id>')
def delete_chain(chain_id: int) -> Response:
    chain_controller.delete(chain_id)
    return make_response("Chain deleted", HTTPStatus.NO_CONTENT)
