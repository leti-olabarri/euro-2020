from app import app
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.jsonfy import jsonfy
from database import db

@app.route("/matches")
@handle_error
def search_all_matches():
    query = f"""
        SELECT row_to_json(matches)
        FROM (
            SELECT *
            FROM "match"
        ) matches
    """
    result = list(db.execute(query))

    matches = jsonfy(result)

    data = {
        "status": "OK",
        "matches": matches
    }
    
    return json_response(data)

@app.route("/matches/<stageParameter>")
@handle_error
def search_matches_by_stage(stageParameter):
    if not stageParameter:
        return {
            "status": "error",
            "message": "No stage, please select one"
        }, 400
    
    query = f"""
        SELECT row_to_json(matches)
        FROM (
            SELECT stage, team_name_home, team_home_score, team_name_away, team_away_score
            FROM "match"
            WHERE stage='{stageParameter}'
        ) matches
    """
    result = list(db.execute(query))

    matches = jsonfy(result)

    data = {
        "status": "OK",
        "matches": matches
    }
    
    return json_response(data)

@app.route("/")
def hello_world():
    return "<p>Come on, your api is working!</p>"
