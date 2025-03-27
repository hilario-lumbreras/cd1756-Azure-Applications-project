from datetime import datetime
from FlaskWebProject import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from azure.storage.blob import BlockBlobService
import string, random
from werkzeug.utils import secure_filename
from flask import flash, current_app
import os

# Blob service setup
blob_container = app.config['BLOB_CONTAINER']
blob_service = BlockBlobService(account_name=app.config['BLOB_ACCOUNT'], account_key=app.config['BLOB_STORAGE_KEY'])

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    """Generates a random string of fixed size."""
    return ''.join(random.choice(chars) for _ in range(size))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """Sets password hash for the user."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the password hash."""
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    """Load user by ID."""
    return User.query.get(int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(75))
    body = db.Column(db.String(800))
    image_path = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post {self.body}>'

    def save_changes(self, form, file, user_id, new=False):
        """Save or update post, including handling image uploads."""
        self.title = form.title.data
        self.author = form.author.data
        self.body = form.body.data
        self.user_id = user_id

        if file:
            try:
                filename = secure_filename(file.filename)
                file_extension = filename.rsplit('.', 1)[1]
                random_filename = id_generator()
                filename = f'{random_filename}.{file_extension}'
                
                # Upload the file to Azure Blob Storage
                blob_service.create_blob_from_stream(blob_container, filename, file)
                
                # If there was an old image, delete it from Blob Storage
                if self.image_path:
                    blob_service.delete_blob(blob_container, self.image_path)
                
                self.image_path = filename
            except Exception as e:
                # Log the error and flash a user-friendly message
                current_app.logger.error(f"Error uploading file: {e}")
                flash('There was an issue uploading the image. Please try again.', 'error')

        # Add the post to the database session
        if new:
            db.session.add(self)
        
        # Commit changes to the database
        db.session.commit()
