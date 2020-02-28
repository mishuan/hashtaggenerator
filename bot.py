from discord.ext import commands

from hashtags import gen_hashtags

DISCORD_TOKEN = "Njc3MzA3NzA3NDMwMTQxOTcz.XlmhJA.Yq-mJA2dnaHkvFE8G-9ry2ncx_A"

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hello', help='Says hello to you.')
async def hello(ctx):
    await ctx.send('Hello')


@bot.command(
    name='hashtags',
    help='Generates hashtags based on parameters passed in.',
)
async def hashtags(ctx, category, count=25):
    htags = gen_hashtags(category, count)
    await ctx.send(htags)

bot.run(DISCORD_TOKEN)
