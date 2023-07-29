from typing import List
import uuid

import strawberry
from strawberry.sanic.views import GraphQLView

from database import get_users, get_tweets, create_user, create_tweet


@strawberry.type
class User:
    id: uuid.UUID
    username: str
    tweets: List["Tweet"]


@strawberry.type
class Tweet:
    id: uuid.UUID
    message: str
    user: User


@strawberry.type
class Query:
    all_users: List[User] = strawberry.field(
        resolver=get_users,
        name="get_users",
        description="Get all Users",
    )
    all_tweets: List[Tweet] = strawberry.field(
        resolver=get_tweets,
        name="get_tweets",
        description="Get all Tweets",
    )


@strawberry.type
class Mutation:
    create_user: User = strawberry.field(
        resolver=create_user,
        name="create_user",
        description="Create a new User",
    )
    create_tweet: Tweet = strawberry.field(
        resolver=create_tweet,
        name="create_tweet",
        description="Create a new Tweet",
    )


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLView.as_view(schema=schema, graphiql=True)
