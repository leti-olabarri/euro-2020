from app import app
import os
import controllers.match_controller
import controllers.club_controller
import controllers.player_controller
import controllers.venue_controller

PORT = int(os.environ.get('PORT', 5000))

app.run("0.0.0.0", PORT, debug=True)