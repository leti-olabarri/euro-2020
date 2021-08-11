from app import app
import controllers.match_controller
import controllers.club_controller
import controllers.player_controller
from config import PORT

app.run("0.0.0.0", PORT, debug=True)