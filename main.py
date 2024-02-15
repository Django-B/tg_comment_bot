from telethon import TelegramClient, tl
import asyncio

api_id = 6024458
api_hash = 'ef40f2f3d50add35b31cf8292d00689e'

bot_token = '5874042173:AAHRf9KErN04hLou7Z-B8kkgl6hpkWh2kcc'


client = TelegramClient('my_session', api_id, api_hash)


async def get_channel_entity(channel: str):
    async with client:
        entity = await client.get_entity(channel)
        return entity

async def parse_post(channel_entity: tl.types.Channel, limit: int = 1):
    '''Возвращает последние посты с канала'''
    async with client:
        posts = await client.get_messages(channel_entity, limit=limit)
        return posts

async def send_comment(channel_entity: tl.types.Channel, post: tl.patched.Message, comment: str):
    '''Оставляет комментарий под постом'''
    async with client:
        await client.send_message(channel_entity, comment, comment_to=post)

async def main():
    channel_name = 'https://t.me/test_channel2077'
    channel_name = 'https://t.me/ithumor'
    channel = await get_channel_entity(channel_name)
    posts = await parse_post(channel)
    await send_comment(channel, posts[0], 'Ахаха')

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
