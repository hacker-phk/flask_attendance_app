from flask import Flask
from models.employee import db
from routes.attendance_routes import attendance_blueprint
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'  # Modify as per your database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Register the attendance blueprint with the app
app.register_blueprint(attendance_blueprint)

# Enable Cross-Origin Resource Sharing (CORS) to allow requests from other domains
CORS(app)

if __name__ == '__main__':
    """
    Main entry point of the application.
    - Creates all necessary database tables when the app starts.
    - Runs the Flask app in debug mode.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()  # Create all database tables as defined in models
    app.run(debug=True)  # Start the Flask development server
