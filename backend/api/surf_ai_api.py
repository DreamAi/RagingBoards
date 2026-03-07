from flask import Blueprint, request, jsonify
from ai.surf_spot_ai import create_board_for_spot

surf_ai_api = Blueprint("surf_ai_api",__name__)

@surf_ai_api.route("/surf-ai",methods=["GET"])
def surf_ai():

    spot = request.args.get("spot")

    result = create_board_for_spot(spot)

    return jsonify(result)
