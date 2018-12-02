from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import at bottom to prevent circular imports
from app import api
from app import routes