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

async def parse_post(channel_entity: tl.types.Channel, limit: int = 3):
    '''Возвращает последние посты с канала'''
    async with client:
        posts = await client.get_messages(channel_entity, limit=limit)
        return posts

async def get_comments(channel_entity, post, limit=10):
    '''Возвращает комментарии под постом'''
    async with client:
        try:
            comments = await client.get_messages(channel_entity, reply_to=post.id, limit=limit)
            return comments
        except Exception as e:
            print('Comments getting error:', e)
            return False

async def send_comment(channel_entity: tl.types.Channel, post: tl.patched.Message, comment: str):
    '''Оставляет комментарий под постом'''
    async with client:
        try:
            await client.send_message(channel_entity, comment, comment_to=post)
            print('Comment sent ✔')
            return True
        except Exception as e:
            print('Comment sending error:', e)
            return False

async def get_chats():
    '''Читает и возвращает список чатов из файла chats.txt'''
    with open('chats.txt') as f:
        chats = f.readlines()
    chats = [chat.strip() for chat in chats]
    return chats

async def main():
    channel_name = 'https://t.me/test_channel2077'
    # channel_name = 'https://t.me/ithumor'
    channel = await get_channel_entity(channel_name)
    posts = await parse_post(channel)
    # await send_comment(channel, posts[0], 'New bot comment')
    # await send_comment(channel, posts[1], 'New bot comment')
    # comments = await get_comments(channel, posts[0])
    # print(comments)
    


if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
