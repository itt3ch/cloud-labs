from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from my_project.auth.controller import panel_video_controller
from my_project.auth.domain.orders.PanelVideo import PanelVideo

panel_video_bp = Blueprint('panel_video', __name__, url_prefix='/panel-video')

@panel_video_bp.get('')
def get_all_panel_videos() -> Response:
    videos = panel_video_controller.find_all()
    videos_dto = [video.put_into_dto() for video in videos]
    return make_response(jsonify(videos_dto), HTTPStatus.OK)

@panel_video_bp.post('')
def create_panel_video() -> Response:
    content = request.get_json()
    video = PanelVideo.create_from_dto(content)
    panel_video_controller.create(video)
    return make_response(jsonify(video.put_into_dto()), HTTPStatus.CREATED)

@panel_video_bp.get('/<int:video_id>')
def get_panel_video(video_id: int) -> Response:
    video = panel_video_controller.find_by_id(video_id)
    if video:
        return make_response(jsonify(video.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Panel video not found"}), HTTPStatus.NOT_FOUND)

@panel_video_bp.put('/<int:video_id>')
def update_panel_video(video_id: int) -> Response:
    content = request.get_json()
    video = PanelVideo.create_from_dto(content)
    panel_video_controller.update(video_id, video)
    return make_response("Panel video updated", HTTPStatus.OK)

@panel_video_bp.delete('/<int:video_id>')
def delete_panel_video(video_id: int) -> Response:
    panel_video_controller.delete(video_id)
    return make_response("Panel video deleted", HTTPStatus.NO_CONTENT)

@panel_video_bp.get('/details')
def get_panel_videos_with_details() -> Response:
    panel_videos = panel_video_controller.find_all_with_details()
    return make_response(jsonify(panel_videos), HTTPStatus.OK)
