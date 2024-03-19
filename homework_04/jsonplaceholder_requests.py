"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(5.0)) as session:
        async with session.get(url) as response:
            return await response.json()


async def get_users():
    return await fetch_json(USERS_DATA_URL)


async def get_posts():
    return await fetch_json(POSTS_DATA_URL)


async def main():
    users, posts = await asyncio.gather(get_users(), get_posts())
    print(len(users), len(posts))


if __name__ == "__main__":
    asyncio.run(main())
