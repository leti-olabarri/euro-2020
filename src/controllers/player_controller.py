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
    "age_min": request.args.get("age_min"),
    "age_max": request.args.get("age_max"),
    "position": request.args.get("position"),
    "matches_min": request.args.get("matches_min"),
    "matches_max": request.args.get("matches_max"),
    "passing_acc_perc_min": request.args.get("passing_acc_perc_min"),
    "passing_acc_perc_max": request.args.get("passing_acc_perc_max"),
    "goals_min": request.args.get("goals_min"),
    "goals_max": request.args.get("goals_max"),
    "fouls_comm_min": request.args.get("fouls_comm_min"),
    "fouls_comm_max": request.args.get("fouls_comm_max"),
    "fouls_suff_min": request.args.get("fouls_suff_min"),
    "fouls_suff_max": request.args.get("fouls_suff_max"),
    "attempts_min": request.args.get("attempts_min"),
    "attempts_max": request.args.get("attempts_max"),
    "attempts_on_target_min": request.args.get("attempts_on_target_min"),
    "attempts_on_target_max": request.args.get("attempts_on_target_max"),
    "assists_min": request.args.get("assists_min"),
    "assists_max": request.args.get("assists_max"),
    "speed_km_h_min": request.args.get("speed_km_h_min"),
    "speed_km_h_max": request.args.get("speed_km_h_max"),
    "balls_recovered_min": request.args.get("balls_recovered_min"),
    "balls_recovered_max": request.args.get("balls_recovered_max"),
    "distance_covered_km_min": request.args.get("distance_covered_km_min"),
    "distance_covered_km_max": request.args.get("distance_covered_km_max"),
    "clearances_min": request.args.get("clearances_min"),
    "clearances_max": request.args.get("clearances_max"),
    "blocks_min": request.args.get("blocks_min"),
    "blocks_max": request.args.get("blocks_max"),
    "saves_min": request.args.get("saves_min"),
    "saves_max": request.args.get("saves_max"),
    "goals_conceded_min": request.args.get("goals_conceded_min"),
    "goals_conceded_max": request.args.get("goals_conceded_max"),
    "clean_sheets_min": request.args.get("clean_sheets_min"),
    "clean_sheets_max": request.args.get("clean_sheets_max")
    }
    
    conditions = ""

    for key, value in stats.items():
        if value:
            if key == "position":
                conditions += f"{key}='{value}' AND "
            elif key[-1] == "x":
                key = key.replace("_max", "")
                conditions += f"{key}<={value} AND "
            else:
                key = key.replace("_min", "")
                conditions += f"{key}>={value} AND "
    size = len(conditions)

    if size == 0:
        conditions = ""
    else:
        conditions = "WHERE " + conditions[:size - 5]
    
    query = f"""
        SELECT row_to_json(players)
        FROM (
            SELECT *
            FROM player
            {conditions}
        ) players
    """
    result = list(db.execute(query))

    players = jsonfy(result)

    data = {
        "status": "OK",
        "players": players
    }
    
    return json_response(data)

