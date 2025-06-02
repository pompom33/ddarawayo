import os
from dotenv import load_dotenv

load_dotenv() # .env 파일을 자동으로 찾아 읽어옴

# TMAP_API_KEY = os.getenv("TMAP_API_KEY") # 실제 배포용
TMAP_API_KEY = os.getenv("TMAP_API_KEY", "FAKE_TMAP_KEY_FOR_TEST") # 개발용

if not TMAP_API_KEY:
    raise ValueError("필수 API 키가 .env 파일에 없습니다!")