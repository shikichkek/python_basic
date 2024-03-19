"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp


USERS_DATA_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            return await response.json()


async def get_users():
    return await fetch_json(USERS_DATA_URL)


async def get_posts():
    return await fetch_json(POSTS_DATA_URL)


async def main():
    await get_users()
    await get_posts()


if __name__ == "__main__":
    asyncio.run(main())
