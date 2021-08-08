import os
import dotenv

dotenv.load_dotenv()

PORT = int(os.getenv("PORT"))
POSTGRES = os.getenv("POSTGRES")