"""Database models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy database instance
db = SQLAlchemy()

# Default image URL for users
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

# Define the User model
class User(db.Model):
    """User model for the Blogly application."""

    # Table name
    __tablename__ = "users"

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    # Property to get the full name of the user
    @property
    def full_name(self):
        """Return the full name of the user."""
        return f"{self.first_name} {self.last_name}"

# Function to connect the database to the Flask app
def connect_db(app):
    """Connect the database to the provided Flask app."""
    db.app = app
    db.init_app(app)
