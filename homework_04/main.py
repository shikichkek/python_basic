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

from typing import List

from jsonplaceholder_requests import get_users, get_posts
from models import User, Post, Base, engine, Session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_users(users):
    users_list = []
    for user in users:
        users_list.append(User(id=user['id'],
                               name=user['name'],
                               username=user['username'],
                               email=user['email']))
    async with Session() as session:
        async with session.begin():
            session.add_all(users_list)


async def insert_posts(posts):
    posts_list = []
    for post in posts:
        posts_list.append(Post(id=post['id'],
                               title=post['title'],
                               user_id=post['userId'],
                               body=post['body']))
    async with Session() as session:
        async with session.begin():
            session.add_all(posts_list)


async def async_main():
    users: List[dict]
    posts: List[dict]
    users, posts = await asyncio.gather(
        get_users(),
        get_posts(),
    )

    await create_tables()
    await insert_users(users)
    await insert_posts(posts)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
