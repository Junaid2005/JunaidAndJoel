import os
import sys


from models import Session
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.logger import logger

class UserService:
    def __init__(self):
        # Initialize session
        self.session = Session()

    def add_user(self, user_id):
        if not self.get_user(user_id):
            try:
                new_user = User(userId=user_id)
                self.session.add(new_user)
                self.session.commit()
                logger.info(f"User {user_id} added successfully!")
            except SQLAlchemyError as e:
                #this rolls back the entire session if something goes wrong (we can discuss later)
                self.session.rollback()
                logger.error(f"Error adding user {user_id}: {e}")
        else:
            logger.error(f"User with {user_id} already exists")

    def get_user(self, user_id):
        try:
            user = self.session.query(User).filter(User.userId == user_id).first()
            return user
        except SQLAlchemyError as e:
            logger.error(f"Error fetching user {user_id}: {e}")
            return None

    def is_admin(self, user_id):
        user = self.get_user(user_id)
        return user is not None and user.admin

    #close the session after you have used the service
    def close(self):
        if self.session:
            self.session.close()
            self.session = None
            logger.info("Session closed.")

