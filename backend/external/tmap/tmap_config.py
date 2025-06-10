import os
from dotenv import load_dotenv

load_dotenv() # .env 파일을 자동으로 찾아 읽어옴

TMAP_API_KEY = os.getenv("TMAP_API_KEY")
TMAP_REQUEST_URL = os.getenv("TMAP_REQUEST_URL")

if not TMAP_API_KEY:
    raise ValueError("TMAP_API_KEY가 .env 파일에 없습니다!")

if not TMAP_REQUEST_URL:
    raise ValueError("TMAP_REQUEST_URL가 .env 파일에 없습니다!")