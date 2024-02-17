from telethon import TelegramClient
from telethon.types import Message
import g4f
import asyncio

api_id = 6024458
api_hash = 'ef40f2f3d50add35b31cf8292d00689e'
client = TelegramClient('my_session', api_id, api_hash)

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
]

_models = [
    g4f.models.gpt_4,
    g4f.models.gpt_4_32k,
    g4f.models.gpt_4_0613,
    g4f.models.gpt_35_long,
    g4f.models.gpt_4_turbo,
    g4f.models.gpt_35_turbo,
    g4f.models.gpt_4_32k_0613,
    g4f.models.gpt_35_turbo_16k,
    g4f.models.gpt_35_turbo_0613,
    g4f.models.gpt_35_turbo_16k_0613,
]



async def parse_post(channel: str, limit: int = 3):
    '''Возвращает последние посты с канала'''
    async with client:
        posts = await client.get_messages(channel, limit=limit)
        return posts

async def get_comments(channel, post: Message, limit=10):
    '''Возвращает комментарии под постом'''
    async with client:
        try:
            comments = await client.get_messages(channel, reply_to=post.id, limit=limit)
            return comments
        except Exception as e:
            print('Comments getting error:', e)
            return False

async def send_comment(channel: str, post: Message, comment: str):
    '''Оставляет комментарий под постом'''
    async with client:
        try:
            await client.send_message(channel, comment, comment_to=post)
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

async def send_to_gpt(prompt: str) -> str | None:
    '''Возвращает ответ GPT на промпт'''
    for provider in _providers:
        try:
            for model in _models:
                try:
                    response = await g4f.ChatCompletion.create_async( # type: ignore
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        provider=provider,
                    )
                    print(f'Model: {model}, Provider: {provider} - it is working')
                    return str(response)
                except Exception as _:
                    # print(f'{model}: is not working')
                    continue
        except Exception as _:
            # print(f'{provider.__name__}: is not working')
            continue



async def main():
    channel = 'https://t.me/test_channel2077'
    channel = 'https://t.me/mama_bond007'
    # channel = 'https://t.me/ithumor'
    # posts = await parse_post(channel)
    # print(posts[0].views) # получение количества просмотров поста
    # print(type(posts[0]))
    # await send_comment(channel, posts[0], 'New bot comment')
    # await send_comment(channel, posts[1], 'New bot comment')
    # comments = await get_comments(channel, posts[0])
    # print(comments)

    response = await send_to_gpt('hello')
    print(response)


    


if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
