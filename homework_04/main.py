"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


import asyncio

from models import User, Post, Base, engine, Session
from jsonplaceholder_requests import get_posts, get_users


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_data():
    return await asyncio.gather(get_users(), get_posts())


def convert_users(users: list[dict]) -> list[User]:
    return [
        User(
            id=item["id"],
            name=item["name"],
            username=item["username"],
            email=item["email"],
        )
        for item in users
    ]


def convert_posts(posts: list[dict]) -> list[Post]:
    return [
        Post(
            id=item["id"],
            user_id=item["userId"],
            title=item["title"],
            body=item["body"],
        )
        for item in posts
    ]


async def write_to_db(entities):
    async with Session() as session:
        async with session.begin():
            session.add_all(entities)


async def async_main():
    await create_tables()
    users_data, posts_data = await get_data()
    users, posts = convert_users(users_data), convert_posts(posts_data)
    await write_to_db(users + posts)
    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
