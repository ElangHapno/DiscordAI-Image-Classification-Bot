import discord
from discord.ext import commands
import random, os, requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checkAI(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            namafile = file.filename
            urlfile = file.url
            await file.save(f'./{namafile}')
            await ctx.send(f'gambar telah disimpan dengan nama {namafile}')

            # KLASIFIKASI DAN INFERENSI
            kelas, skor = get_class('keras_model.h5', 'labels.txt', namafile)

            if kelas == 'kucing telinga runcing\n' and skor >= 0.75:
                await ctx.send('Ini adalah kucing telinga runcing')
                await ctx.send('selain telinga nya runcing')
                await ctx.send('telinga-telinga tersebut sangatlah tinggi')
                await ctx.send('tapi lumayan buat dimakan')
            elif kelas == 'kucing telinga lipat\n' and skor >= 0.75:
                await ctx.send('ini adalah kucing telinga lipat')
                await ctx.send('kucing telinga lipat ini sangatlah lucu')
                await ctx.send('alian gemes dan ngeselin banget')
                await ctx.send('tapi lumayan buat dimakan')
            else:
                await ctx.send('Ini mah sich bahaya banget ga sich?')
    else:
        await ctx.send('mana gambarnya?')

bot.run("")
