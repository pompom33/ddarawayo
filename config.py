# 데이터베이스 사용을 위해 config.py 파일을 사용한다(위치는 backend 모듈 밖이여야 함)

import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = DB 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'StationFacilities.db'))

# SQLALCHEMY_TRACK_MODIFICATIONS = 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False