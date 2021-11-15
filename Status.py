import discord
from discord.ext import commands

token = "Token" #Your Token

#index---
bot = commands.Bot(command_prefix = "123456789")

print("\033[1;33;40m_________________________________________________ ")
print("Tool")
print("▒█▀▀▀█ ▀▀█▀▀ █▀▀█ ▀▀█▀▀ █░░█ █▀▀ 　 ▒█░▒█ ▒█▀▀█ ")
print("░▀▀▀▄▄ ░░█░░ █▄▄█ ░░█░░ █░░█ ▀▀█ 　 ▒█░▒█ ▒█▄▄█ ")
print("▒█▄▄▄█ ░░▀░░ ▀░░▀ ░░▀░░ ░▀▀▀ ▀▀▀ 　 ░▀▄▄▀ ▒█░░░")
print("__________________________________________________ \n")
print("\033[1;36;40m            Status Free By Jonathan \n")
print("\033[1;35;40m            DEV BY Jonathan Jackson \n")
print("\033[1;33;40m__________________________________________________ \n")
print("\033[1;39;40m  Type what you want to display as Status")     
status = input(' [✓]-------------[>] ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/monstercat'
    )
    print('Streaming [✓] ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)    
#how to use
 #Termux type python Status.py
 #If using a computer, open cmd and type   #python Status.py
 #Don't forget to edit the 4th line first.