from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# 전역 변수
StationFacilitiesDB = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) # config.py에 작성한 항목을 'app.config' 환경 변수로 부르기 위함

    # ORM
    StationFacilitiesDB.init_app(app)
    migrate.init_app(app, db=StationFacilitiesDB)

    # Blueprint
    from backend.views import main_views
    app.register_blueprint(main_views.bp)

    return app