
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 60 * 24 * 7))  # 7 days
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "changeme123")
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY", "refreshchangeme456")
ALGORITHM = "HS256"
