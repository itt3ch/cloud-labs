from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import video_producer_controller
from my_project.auth.domain.orders.VideoProducer import VideoProducer

video_producer_bp = Blueprint('video_producer', __name__, url_prefix='/video_producer')

@video_producer_bp.get('')
def get_all_producers() -> Response:
    producers = video_producer_controller.find_all()
    producers_dto = [producer.put_into_dto() for producer in producers]
    return make_response(jsonify(producers_dto), HTTPStatus.OK)

@video_producer_bp.post('')
def create_producer() -> Response:
    content = request.get_json()
    producer = VideoProducer.create_from_dto(content)
    video_producer_controller.create(producer)
    return make_response(jsonify(producer.put_into_dto()), HTTPStatus.CREATED)

@video_producer_bp.get('/<int:producer_id>')
def get_producer(producer_id: int) -> Response:
    producer = video_producer_controller.find_by_id(producer_id)
    if producer:
        return make_response(jsonify(producer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Producer not found"}), HTTPStatus.NOT_FOUND)

@video_producer_bp.put('/<int:producer_id>')
def update_producer(producer_id: int) -> Response:
    content = request.get_json()
    producer = VideoProducer.create_from_dto(content)
    video_producer_controller.update(producer_id, producer)
    return make_response("Producer updated", HTTPStatus.OK)

@video_producer_bp.delete('/<int:producer_id>')
def delete_producer(producer_id: int) -> Response:
    video_producer_controller.delete(producer_id)
    return make_response("Producer deleted", HTTPStatus.NO_CONTENT)
