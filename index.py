import discord
from discord.ext import commands
import asyncio
import random
from random import randint
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import Bot
from pistonapi import PistonAPI
from PIL import Image
from PIL.Image import core as _imaging
from PIL import *
from PIL import Image, ImageDraw, ImageFont
from discord.ext.commands import Cog
from discord.utils import get


piston = PistonAPI()
TOKEN = "YOUR_TOKEN_HERE"

intents = discord.Intents.all()
intents.reactions = True


activity = discord.Game(name="Chilling")

bot = commands.Bot(command_prefix = ";", description = "Chilling", help_command=None, intents = intents, activity=activity, status=discord.Status.idle)
client = discord.Client(intents=intents)



@bot.event
async def on_ready():
    print("Ready !")



@bot.command(aliases = ["serverinfo", "Serverstatus", "serverstats", "ServerInfo"])
async def serverInfos(ctx):
	server = ctx.guild
	NumberTXTchannels = len(server.text_channels)
	NumberVoiceChannels = len(server.voice_channels)
	NumberPeople = server.member_count
	ServerName = server.name
	message = f"The server **{ServerName}** currently contains : \n - {NumberTXTchannels} text channels, \n - {NumberVoiceChannels} voice channels. \n - The server has {NumberPeople} members !"
	await ctx.send(message)



@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	embed = discord.Embed(description = f"{user} was **banned** !")
	embed.set_image(url = "https://i.pinimg.com/originals/a8/e6/82/a8e6827795233d003a64996fb592fdbd.gif")
	embed.set_footer(text = f"raison: {reason}")
	await ctx.send(embed = embed)


@bot.command(name='unban')
@has_permissions(administrator = True)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f"{user} just got unbanned")

@bot.command()
@has_permissions(administrator = True)
async def gcreate(ctx, time = None, *, prize=None):
	if time == None:
		return await ctx.send("Please indicate a duration !")
	elif prize == None:
		return await ctx.send("Please indicate the prize !")
	embed = discord.Embed(title='New Giveaway !', description = f"{ctx.author.mention} puts **{prize}** into play !")
	time_convert = {"s":1, "m":60, "h":3600, "d":86400}
	gawtime = int(time[0]) * time_convert[time[-1]]
	embed.set_footer(text = f"The giveaway ends in {time}")
	gaw_msg = await ctx.send(embed = embed)

	await gaw_msg.add_reaction("🎉")
	await asyncio.sleep(gawtime)

	new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

	users = await new_gaw_msg.reactions[0].users().flatten()
	users.pop(users.index(bot.user))

	winner = random.choice(users)

	await ctx.send(f"**🎉 {winner.mention} is the winner !**")

@bot.command()
async def bang(ctx, user : discord.User):
	pictures = ["https://cdn.weeb.sh/images/S1-RQVFjZ.gif","https://cdn.weeb.sh/images/SkFub87DW.gif","https://cdn.weeb.sh/images/BJADXEtoZ.gif","https://cdn.weeb.sh/images/Sk3v-LmD-.gif","https://cdn.weeb.sh/images/BkWIXNFo-.gif","https://media1.tenor.com/images/ffc687154704c3a1b77dcfe8566b3312/tenor.gif?itemid=15110183","https://media.tenor.com/images/b218a30ff0fc31a170dd6f99aa3899cd/tenor.gif",
	"https://media.tenor.com/images/39e2de4a64414916c87a55b6c8af3427/tenor.gif","https://media.tenor.com/images/ef9962e338e2148860d4d1522040142d/tenor.gif","https://media.tenor.com/images/29145d2d2903a529aebfb343722ce841/tenor.gif","https://media.tenor.com/images/7e4b9d9fa9a8de2b9816e27f617f57d3/tenor.gif"]


	embed=discord.Embed(description = f"{ctx.author.mention} banged {user.mention} !")
	embed.set_image(url = random.choice(pictures))

	await ctx.send(embed = embed)

@bot.command()
async def hug(ctx, user : discord.User):
	pictures = ["https://media.tenor.com/images/8f44c083c55620c02f59c6bea378dca4/tenor.gif","https://media.tenor.com/images/6083ba11631dd577bcc271268d010832/tenor.gif","https://media.tenor.com/images/9fe95432f2d10d7de2e279d5c10b9b51/tenor.gif",
	"https://media.tenor.com/images/a9bb4d55724484be94d13dd94721a8d9/tenor.gif","https://media.tenor.com/images/61ea96bce16c53a913336a3dbc1a6100/tenor.gif","https://media.tenor.com/images/68af867e8e0a1c5e7574c4d7f9d90a44/tenor.gif",
	"https://media.tenor.com/images/d3408c3acb2f3e5223105a722084b182/tenor.gif","https://media.tenor.com/images/59bd16406f4e5c78fb5caf51ce446e76/tenor.gif","https://media.tenor.com/images/1440b89a2590bdee99b1a29c0ee8e5d1/tenor.gif"]

	embed=discord.Embed(description = f"{ctx.author.mention} hugged {user.mention} !")
	embed.set_image(url = random.choice(pictures))

	await ctx.send(embed = embed)

@bot.command(saliaes = ["8ball", "answers", "answer"])
async def question(ctx):

	answers = ["probably :smirk:", "possibly !", "No, definitely not.", "There are chances", "Indeed", "Of course !", "Yes !", "No."]
	answer = random.choice(answers)
	await ctx.send(answer)

@bot.command(aliases = ["love", "pronostics", "pronostic"])
async def ship(ctx, user : discord.User):
	love = randint(1, 100)
	choicegif = ""
	if love < 31:
		choicegif = "https://media.tenor.com/images/290d78917d434abd580cc8036d45a437/tenor.gif"
	elif love > 30 and love < 60:
		choicegif = "https://media.tenor.com/images/618f7f69e26c56dd92b5f0e16d163946/tenor.gif"
	elif love >=60:
		choicegif = "https://media.tenor.com/images/74a2b4b0fc38bc87c81f68b0bb24572d/tenor.gif"

	embed = discord.Embed(description = f"{ctx.author.mention} et {user} vous êtes compatibles à **{love}%** !")
	embed.set_image(url = choicegif)
	await ctx.send(embed = embed)

@bot.command()
async def jojo(ctx):

	jojo = ["https://cdn.weeb.sh/images/ByN3aOQvb.png", "https://cdn.weeb.sh/images/Hyxl3aOmDb.png", "https://cdn.weeb.sh/images/Syi36_mwb.png",
	"https://cdn.weeb.sh/images/rykM3brrM.gif", "https://cdn.weeb.sh/images/r1-h6dQvb.jpeg", "https://cdn.weeb.sh/images/HJq3TuQw-.gif"]
	jojopost = random.choice(jojo)
	embed = discord.Embed()
	embed.set_image(url = jojopost)
	await ctx.send(embed = embed)

@bot.command()
async def run(ctx, n, *, code):
  nm = n.lower()
  a = code.replace("```","")

  if nm=="py":
      b = (piston.execute(language="py", version="3.9", code=a))
      c = str(b)
      em = discord.Embed(title="Python Code Output!", 
        description=f'```py\nOutput:\n{c}```',
        color=discord.Color.red())
      
  elif nm=="java":
      b = (piston.execute(language="java", version="15.0.2", code=a))
      c = str(b)
      em = discord.Embed(title="Java Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
      
  elif nm=="js":
      b = (piston.execute(language="js", version="15.10.0", code=a))
      c = str(b)
      em = discord.Embed(title="JavaScript Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
      
  elif nm=="go":
      b = (piston.execute(language="go", version="1.16.2", code=a))
      c = str(b)
      em = discord.Embed(title="Go Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
 
  elif nm=="ts":
      b = (piston.execute(language="typescript", version="4.2.3", code=a))
      c = str(b)
      em = discord.Embed(title="TypeScript Code Output!", 
        description=f'```py\nOutput:\n{c}```',
        color=discord.Color.red())
     
  elif nm=="bf":
      b = (piston.execute(language="brainfuck", version="2.7.3", code=a))
      c = str(b)
      em = discord.Embed(title="BrainFuck Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
      
  else:
      em = discord.Embed(title="**Not a supported language!!**")

  await ctx.send(embed=em)


@bot.command()
async def run_lang(ctx):
	embed = discord.Embed(description = "> Available languages :\n-python: 'py'\n-java\n-javascript: 'js'\n-go\n-typescript: 'ts'\n-brainfuck: 'bf'\n\n*note that the aliases (like 'py' for python) are how you have to call them when using the command 'run'.*\n")
	embed.set_footer(text = "*Versions : python-3.9, java-15.0.2, js-15.10.0, go-1.16.2, typescript-4.2.3, brainfuck-2.7.3*")
	await ctx.send(embed = embed)



@bot.command()
async def help(ctx):
	embed = discord.Embed(description = "> Main Command :\n- run <lang> ('help_run' for more infos)\n> Usefull Commands :\n- serverInfos\n - ban\n- unban <user_id>\n> Fun Commands :\n- bang\n- hug\n- 8ball\n- ship\n- jojo\n- poll\n")
	embed.set_footer(text = "Note : you can use the 'help_run' command to see how the run command workrs.")
	await ctx.send(embed = embed)

@bot.command()
async def help_run(ctx):
	embed = discord.Embed(title = "Run helper", description = "The 'run' command allows you to see the result of a script / snippet in a language. It allows for example to see what a python script would produce.\n  Here's the syntax of the command: ```<prefix>run py <My_Code> ``` (The code has to be between ```).\nYou can of course run other languages than python.")
	embed.set_footer(text = "type '<prefix>run_lang' to access the list of available languages.")
	await ctx.send(embed = embed)

# A meme command, just type <prefix>trainmeme <first_text>, <second_text>

@bot.command()
async def trainmeme(ctx, *, text):
	text = text.split(",")
	text2 = text[0]
	text3 = text[1]
	img = Image.open("assets/train.jpg")
	draw = ImageDraw.Draw(img)
	drawer = ImageDraw.Draw(img)
	font = ImageFont.truetype("assets/Arimo.ttf", 15)
	drawer.text((80, 55), text=text2, font=font)
	draw.text((30, 185), text=text3, font=font)
	img.save("assets/train1.jpg")
	img.paste(img, (7, 5))
	await ctx.send(file = discord.File("assets/train1.jpg"))

# A meme command, just type <prefix>yeetmeme <text>

@bot.command()
async def yeetmeme(ctx, *, text):
	text = text.split(",")
	text2 = text[0]
	img = Image.open("assets/yeet.png")
	drawer = ImageDraw.Draw(img)
	font = ImageFont.truetype("Arimo.ttf", 35)
	drawer.text((1000, 375), text=text2, font=font, fill='black')
	img.save("assets/yeet1.png")
	img.paste(img, (7, 5))
	await ctx.send(file = discord.File("assets/yeet1.png"))


bot.run(TOKEN)