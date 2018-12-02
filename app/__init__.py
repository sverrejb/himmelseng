from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import at bottom to prevent circular imports
from app import routes