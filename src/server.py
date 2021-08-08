from app import app
import controllers.match_controller
from config import PORT

app.run("0.0.0.0", PORT, debug=True)