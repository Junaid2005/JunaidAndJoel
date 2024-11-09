import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.logger import logger


def loadUsers():
    cursor.execute(
        """
        SELECT userId from users
    """
    )
    users = cursor.fetchall()
    userIds = [user[0] for user in users]
    return userIds


def initUser(id):
    cursor.execute(
        """
        INSERT INTO users (userId)
        VALUES (?)
    """,
        (id,),
    )
    conn.commit()
    logger.info("User initialised")


def isAdmin(id):
    cursor.execute(
        """
        SELECT admin FROM users WHERE userId = ?
        """,
        (id,),
    )
    result = cursor.fetchone()
    return True if result is not None and result[0] == 1 else False


def setAdmin(id, state):
    cursor.execute(
        """
        UPDATE users
        SET admin = ?
        WHERE userId = ?
        """,
        (state, id),
    )
    conn.commit()
    logger.info(f"User {id} admin status set to {state}")


def raw(query):
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    logger.info(f"Raw SQL executed: {result}")
    return result


def decrementWin(id):
    cursor.execute(
        """
        UPDATE users
        SET wins = wins - 1
        WHERE userId = ?
        """,
        (id,),
    )
    conn.commit()
    logger.info(f"User {id} wins decremented by 1")


def incrementWin(id):
    cursor.execute(
        """
        UPDATE users
        SET wins = wins + 1
        WHERE userId = ?
        """,
        (id,),
    )
    conn.commit()
    logger.info(f"{id} wins incremented by 1")


def init():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            userId INTEGER PRIMARY KEY,
            admin BOOLEAN NOT NULL DEFAULT (0),
            wins INTEGER NOT NULL DEFAULT (0) 
        );
    """
    )
    conn.commit()
    logger.info("db initialised successfully")


def close():
    conn.close()


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

init()

close()
