import discord
import openai
client = discord.Client()
openai.api_key = '-'
token = 'MTEzMTUxMDg4MTIxODQ2NTg2Mw.GqXxLK.tfmn5tBETCTa-MWIhITPClt0818mIYJLS1UZPg'
count = 0
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == "!help":
        await message.channel.send('Search for swear words')

    elif message.content.lower().find('fuck') > -1:
        await message.channel.send("don't swear")

    elif message.content.startswith('$chatpt'):
        '''
        model_engine = "text-davinci-003"
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=message.content.replace('!?chatpt', ""),
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        await message.channel.send(completion.choices[0].text)
        print(completion.choices[0].text)
        '''
        await message.channel.send()

    elif message.content.lower().find('chatgpt') > -1:
        await message.channel.send("https://t.me/GPT4Telegrambot")

    elif message.content.lower().find('whatsapp') > -1:
        await message.channel.send("https://web.whatsapp.com/")
    else:
        print('Error :(')
    print(message.author.mention)
client.run(token)