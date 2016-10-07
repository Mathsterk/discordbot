import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.casefold().startswith('top10anime') or message.content.casefold().startswith('topp10anime') or message.content.casefold().startswith('top 10 anime') or message.content.casefold().startswith('topp 10 anime'):
        for i in range(10, 0, -1):
            await client.send_message(message.channel, str(i) + '. ' + 'Naruto')
            await asyncio.sleep(i*0.1)
            print('kuk')

    elif message.content.casefold().startswith('i am a gril'):
            await client.send_message(message.channel, 'sugoi sugoi desu')
            await asyncio.sleep(0.3)
            await client.send_message(message.channel, 'desu watashi wa')
            await asyncio.sleep(0.3)
            await client.send_message(message.channel, 'desu desu konicheewaa')
            await asyncio.sleep(0.3)
            await client.send_message(message.channel, 'arigato san kun')
            await asyncio.sleep(0.3)
            await client.send_message(message.channel, 'desudesukunsan')
            print('pikk')
    elif message.content.casefold().startswith('how 2 be otaku 101'):
            await client.send_message(message.channel, 'https://youtu.be/YvLsWydCkzQ')


client.run('MjA3OTQzNDA5NjQ4OTI2NzIw.CtmkqA.9_AO259ZRrlDILQaA5yPd-WZ_2Y')
