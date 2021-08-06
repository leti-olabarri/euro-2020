import os
import dotenv

dotenv.load_dotenv()

PORT = os.getenv("PORT")
POSTGRES = os.getenv("POSTGRES")