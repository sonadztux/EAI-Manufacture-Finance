from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
swagger_url = '/api/docs'
api_url = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(swagger_url, api_url, config={
    'app_name': 'Manufacture-Finance Transactions REST API'
})

app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

from app.model import transaction
from app import routes