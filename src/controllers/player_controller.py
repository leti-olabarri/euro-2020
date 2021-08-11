from typing import SupportsIndex
from app import app
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.jsonfy import jsonfy
from database import db
from flask import request

@app.route("/player/<playerParameter>")
@handle_error
def find_single_player(playerParameter):
    if not playerParameter:
        return {
            "status": "error",
            "message": "No player, please select one"
        }, 400
    query = f"""
        SELECT row_to_json(players)
        FROM (
            SELECT *
            FROM player
            WHERE "name"='{playerParameter}'
        ) players
    """
    result = list(db.execute(query))

    player = jsonfy(result)

    if len(player) == 0:
        return {
            "status": "error",
            "message": "That player did not player in the UEFA Euro. Check your spelling"
        }, 404

    data = {
        "status": "OK",
        "player": player
    }
    
    return json_response(data)

@app.route("/player/stats")
@handle_error
def filter_players_by_stats():
    stats = {
    "position": request.args.get("position"),
    "matches": request.args.get("matches"),
    "minutes": request.args.get("minutes"),
    "yellow_cards": request.args.get("yellow_cards"),
    "red_cards": request.args.get("red_cards"),
    "passing_acc_perc": request.args.get("passing_acc_perc"),
    "goals": request.args.get("goals"),
    "fouls_comm": request.args.get("fouls_comm"),
    "fouls_suff": request.args.get("fouls_suff"),
    "attempts": request.args.get("attempts"),
    "attempts_on_target": request.args.get("attempts_on_target"),
    "assists": request.args.get("assists"),
    "speed_km_h": request.args.get("speed_km_h"),
    "tackles": request.args.get("tackles"),
    "balls_recovered": request.args.get("balls_recovered"),
    "distance_covered_km": request.args.get("distance_covered_km"),
    "clearances": request.args.get("clearances"),
    "blocks": request.args.get("blocks"),
    "saves": request.args.get("saves"),
    "goals_conceded": request.args.get("goals_conceded"),
    "claims": request.args.get("claims"),
    "punches": request.args.get("punches"),
    "clean_sheets": request.args.get("clean_sheets")
    }

    conditions = ""

    for key, value in stats.items():
        if value:
            if key == "position":
                conditions += f"{key}='{value}' AND "
            else:
                conditions += f"{key}{value} AND "
    
    size = len(conditions)

    if size == 0:
        conditions = ""
    else:
        conditions = "WHERE" + conditions[:size - 5]
    
    query = f"""
        SELECT row_to_json(players)
        FROM (
            SELECT *
            FROM player
            {conditions}
        ) players
    """

    result = list(db.execute(query))

    player = jsonfy(result)

    data = {
        "status": "OK",
        "player": player
    }
    
    return json_response(data)

