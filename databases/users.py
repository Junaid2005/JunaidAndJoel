import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.logger import logger


class UserDB:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        self.init()

    def init(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                userId INTEGER PRIMARY KEY,
                admin BOOLEAN NOT NULL DEFAULT (0),
                wins INTEGER NOT NULL DEFAULT (0)
            );
            """
        )
        self.conn.commit()
        logger.info("DB initialised successfully")

    def raw(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.conn.commit()
        logger.info(f"Raw SQL executed: {query}")
        return result

    def loadUsers(self):
        self.cursor.execute("SELECT userId FROM users")
        users = self.cursor.fetchall()
        user_ids = [user[0] for user in users]
        return user_ids

    def initUser(self, user_id):
        self.cursor.execute(
            """
            INSERT INTO users (userId)
            VALUES (?)
            """,
            (user_id,),
        )
        self.conn.commit()
        logger.info(f"User {user_id} initialized")

    def isAdmin(self, user_id):
        self.cursor.execute(
            """
            SELECT admin FROM users WHERE userId = ?
            """,
            (user_id,),
        )
        result = self.cursor.fetchone()
        return result is not None and result[0] == 1

    def setAdmin(self, user_id, state):
        self.cursor.execute(
            """
            UPDATE users
            SET admin = ?
            WHERE userId = ?
            """,
            (state, user_id),
        )
        self.conn.commit()
        logger.info(f"User {user_id} admin status set to {state}")

    def decrementWin(self, user_id):
        self.cursor.execute(
            """
            UPDATE users
            SET wins = wins - 1
            WHERE userId = ?
            """,
            (user_id,),
        )
        self.conn.commit()
        logger.info(f"User {user_id} wins decremented by 1")

    def incrementWin(self, user_id):
        self.cursor.execute(
            """
            UPDATE users
            SET wins = wins + 1
            WHERE userId = ?
            """,
            (user_id,),
        )
        self.conn.commit()
        logger.info(f"User {user_id} wins incremented by 1")

    def close(self):
        self.conn.close()
        logger.info("DB connection closed")
