import os
import dotenv

dotenv.load_dotenv()

API_URI = os.getenv("API_URI", "https://uefa-euro-2020.herokuapp.com")
