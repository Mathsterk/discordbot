import discord
import asyncio

client = discord.Client()

discord.opus.load_opus("/usr/lib/x86_64-linux-gnu/libopus.so.0")

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


    elif message.content.casefold().startswith("the song"):
        print("faen")
        voice = await client.join_voice_channel(discord.Object(id="207937363517767681"))
        player = voice.create_ffmpeg_player('fisk.mp3')
        player.start()
        await asyncio.sleep(8.7666)
        await voice.disconnect()

    if "mario" in message.content.casefold():
        print("mario")
        voice = await client.join_voice_channel(discord.Object(id="207937363517767681"))
        player = voice.create_ffmpeg_player('mariodeath.wav')
        player.start()
        await asyncio.sleep(3.4)
        await voice.disconnect()

    if "tromme" in message.content.casefold():
        print("luigi")
        voice = await client.join_voice_channel(discord.Object(id="207937363517767681"))
        player = voice.create_ffmpeg_player('trommelyd.wav')
        player.start()
        await asyncio.sleep(4.8)
        await voice.disconnect()

    if "varsel" in message.content.casefold():
        print("whoop whoop")
        voice = await client.join_voice_channel(discord.Object(id="207937363517767681"))
        player = voice.create_ffmpeg_player('mariowarning.mp3')
        player.start()
        await asyncio.sleep(3.2)
        await voice.disconnect()




#    if player.is_done():
 #           voice.disconnect()


client.run('MjA3OTQzNDA5NjQ4OTI2NzIw.CtmkqA.9_AO259ZRrlDILQaA5yPd-WZ_2Y')
