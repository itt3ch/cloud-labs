from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import advertisement_video_controller
from my_project.auth.domain.orders.AdvertisementVideo import AdvertisementVideo

advertisement_video_bp = Blueprint('advertisement_video', __name__, url_prefix='/advertisement_video')

@advertisement_video_bp.get('')
def get_all_videos() -> Response:
    videos = advertisement_video_controller.find_all()
    videos_dto = [video.put_into_dto() for video in videos]
    return make_response(jsonify(videos_dto), HTTPStatus.OK)

@advertisement_video_bp.post('')
def create_video() -> Response:
    content = request.get_json()
    video = AdvertisementVideo.create_from_dto(content)
    advertisement_video_controller.create(video)
    return make_response(jsonify(video.put_into_dto()), HTTPStatus.CREATED)

@advertisement_video_bp.get('/<int:video_id>')
def get_video(video_id: int) -> Response:
    video = advertisement_video_controller.find_by_id(video_id)
    if video:
        return make_response(jsonify(video.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Video not found"}), HTTPStatus.NOT_FOUND)

@advertisement_video_bp.put('/<int:video_id>')
def update_video(video_id: int) -> Response:
    content = request.get_json()
    video = AdvertisementVideo.create_from_dto(content)
    advertisement_video_controller.update(video_id, video)
    return make_response("Video updated", HTTPStatus.OK)

@advertisement_video_bp.delete('/<int:video_id>')
def delete_video(video_id: int) -> Response:
    advertisement_video_controller.delete(video_id)
    return make_response("Video deleted", HTTPStatus.NO_CONTENT)
