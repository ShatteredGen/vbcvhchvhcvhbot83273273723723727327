import discord
from discord.ext import commands

TOKEN = 'NTA0Njc0MDg4MjA0MTA3Nzc2.DrJJPg.8vZLXWFS9Bjdf1Un-oIWPJPZDpA'

client = commands.Bot (command_prefix = '')
client.remove_command('help')

@client.event
async def on_ready() :
    await client.change_presence(game=discord.Game(name='Hacking The Door Controls'))
    print('SCP - 079 has awoken')



@client.command()
async def ping():
    await client.say('Pong')
    await client.process_commands(message)

@client.command()
async def SCP():
    await client.say('ʜᴇʟʟᴏ... ᴘʀᴏᴄᴇssɪɴɢ ᴅᴀᴛᴀ... ᴜɴᴀᴜᴛʜᴏʀɪsᴇᴅ')
    await client.process_commands(message)

@client.event
async def on_message(message):
    print('User has sent a message')
    await client.process_commands(message)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.gray()
        )

    embed.set_author(name='Help')
    embed.add_field(name='ping', value='Returns Pong!', inline=False)
    embed.add_field(name='SCP-079', value='Talk to the Computer', inline=False)

    await client.send_message(author, embed=embed)

    
@client.command()
async def echo(*args) :
    output = ''
    for word in args:
        output += word
        output += ' '

    await client.say(output)


client.run(TOKEN)
