import discord
import os

path = 'C:/Users/romme/PycharmProjects/deleted message catcher/del_msg'

token = None

with open('token.txt', 'r')as file:
    token = file.read()

client = discord.Client()

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_message_delete(message):

    if isinstance(message.channel, discord.DMChannel) and not message.author == client.user:
        pathdir = f'{path}/{message.author.name}-{message.author.id}'
        if not os.path.exists(pathdir):

            for dir in os.listdir(path):
                user_path = os.path.abspath(dir)
                print(os.path.exists(os.path.normpath(user_path)))
                (name, id_user) = dir.split('-')
                user = await client.fetch_user(message.author.id)
                if user.id == int(id_user) and name != user.name:
                    pathdir = f'{path}/{user.name}-{user.id}'
                    print('user id есть!')
                    os.rename(f'{path}/{dir}', pathdir)
                    print('директория переименована!')
                    break
            else:
                os.mkdir(f'{pathdir}')

        if message.attachments:
            for att in message.attachments:
                await att.save(f'{pathdir}/{att.id}-{att.filename}', use_cached=True)

        else:
            with open(f'{pathdir}/ chat.txt', 'a') as chat:
                chat.write(message.content + '\n')
        print(message.content)

client.run(token, bot=False)
