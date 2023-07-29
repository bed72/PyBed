from typing import List
import uuid

from models import User, Tweet


def get_users() -> List[User]:
    return User.select()


def get_tweets() -> List[Tweet]:
    return Tweet.select()


def create_user(username: str) -> User:
    return User.create(username=username)


def create_tweet(user_id: uuid.UUID, message: str) -> Tweet:
    return Tweet.create(message=message, user=user_id)
