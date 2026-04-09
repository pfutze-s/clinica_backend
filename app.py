from flask import Flask
from config.database import Base, engine

from models.user import User
from models.animal import Animal
from models.tutor import Tutor
from routes.auth_routes import auth_bp
from routes.animal_routes import animal_bp
from routes.tutor_routes import tutor_bp

app = Flask(__name__)

Base.metadata.create_all(engine)

app.register_blueprint(animal_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(tutor_bp)

if __name__ == "__main__":
    app.run(debug=True)
