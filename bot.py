import discord
from discord.ext import commands
import youtube_dl
import os
import random

client = commands.Bot(command_prefix=".|. ")

#------------------------Roasts-----------------------
@client.command()
async def roast(ctx,palavra : str):
  if palavra == "meixedo":
        await ctx.send("----")
  elif palavra == "santi":
        await ctx.send("----")
  elif palavra == "machado":
        await ctx.send("----")
  elif palavra == "moreira":
        await ctx.send("----")
  elif palavra == "soveral":
        await ctx.send("----s")
  elif palavra == "carvalho":
        await ctx.send("----")
  elif palavra == "hugo":
        await ctx.send("----?")   
  elif palavra == "f1":
        await ctx.send("----")
      
@client.command()
async def states(ctx):
  await ctx.send("----")
  await ctx.send("----")
  await ctx.send("----")
#------------------------Status-----------------------
@client.command()
async def twitch(ctx,nome : str,link:str):
  nome=nome.replace("|"," ")
  try:
    await client.change_presence(activity=discord.Streaming(name=nome, url=link))
    await ctx.send("Status alterado para a stream de "+nome)
  except:
    await ctx.send("Introduziste mal os dados, .|. twitch (nome) (link da stream)")
@client.command()
async def status(ctx,palavra : str,palavra1:str):
  palavra1=palavra1.replace("|"," ")
  try:
    if palavra=="song":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=palavra1))
      await ctx.send("A ouvir "+palavra1)
    elif palavra=="game":
      await client.change_presence(activity=discord.Game(name=palavra1))
      await ctx.send("A jogar  "+palavra1)
    elif palavra=="movie":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=palavra1))
      await ctx.send("A ver  "+palavra1)
  except:
      await ctx.send("Erro, .|. (song|game|movie) (nome)")

#------------------------Musica-----------------------
def musicas(a):
    if a[0:5] == "bocas":
        nome = a[6:len(a)-1]
        a = str(random.randint(1, 4))
    dic = {
        "hinolei":
        "É ferro, é aço, é merda ao calhamaço\nInformatica marca o passo\nQuem foi? Quem viu?P´rá puta que os pariu\nEu bem dizia que era grossa e não cabia\nEra a maior de toda a academia\nPassou passou passou passou passou ao lado\nTenham cuidado senão são enrabados\nEu bem te disse que ela era pneumática\nA maior piça é a piça de **informática**",
        "atirei":
        "Atirei o pau à gata ta Mas a gata ta\nMas a gata ta,não mordeu eu eu\n Oh minha puta ta,\nPõe-te de quatro tro\nQue já vais ver o que é foder com um informático!\nEla fez-me um cafoné né né\nE mesmo assim sim sim, ficou de pé pé pé\nOh minha puta ta,`tra vez de quatro tro,\nQue vais levar mais uma vez com um informático",
        "hinopoloii":
        "Dos colhões,\nEu fiz um barco, e dos pintelhos\nna armação, a armação\nDos chatos, os tripulantes\ne do caralho, o capitão, o capitão\nNós só queremos:\ncerveja p'ra beber (O QUÊ?)\ncerveja p'ra beber (O QUÊ?)\ncerveja p'ra beber\nNós só queremos:\ncerveja p'ra beber (O QUÊ?)\ncerveja p'ra beber (O QUÊ?)\nE gajas p'ra foder",
        "1":
        "Dizem que ´curso´ é homem\n´curso´ não é homem não\nHomem tem um buraquinho\n´curso´ tem um buracão",
        "2":
        "´curso´ é nosso amigo\n´curso´ é nosso colega\nvamos fazer com ´curso´\no que o cavalo faz com a égua",
        "3":
        "´curso´ comem-se uns aos outros\n´curso´ gostam e não é pouco\n´curso´ são uns panisgões\n´curso´ não têm colhões",
        "4":
        "Comer maminhas,\ncomer bujões é o almoço dos campeões!\nE oh ´curso´! se queres comer,\ncome no cu vai te foder!!\nAllez allez, allez allez, allez allez, allez\nallez!\nE oh ´curso´! se queres comer,\ncome no cu vai te foder\n"
    }
    for i, j in dic.items():
        if a == i:
            if a == "1" or a == "2" or a == "3" or a == "4":
                result = ""
                c = 0
                for i in range(len((j))):
                    if j[i:i + 7] == "´curso´":
                        result += j[c:i]
                        result += nome
                        c = i + 7
                result += j[c:]
                return result
            else:
                return j

@client.command()
async def musica(ctx, palavra : str):
  if palavra == 'album':
    await ctx.send("Escolhe uma: HinoLEI | Atirei | HinoPoloII | Bocas")
  else:
    try:
      await ctx.send(musicas(palavra.lower()))
    except:     
      await ctx.send(palavra.lower())


@client.command()
async def pokemon(ctx, palavra : str):
  if palavra=="leaderbord":
      pontos = {"Bernas": 1,
      "Folhas": 0,
      "Carvalho": 0,
      "Vasques": 1,
      "Alves": 0,
      "Pino": 0,
      "Martim": 0,
      }
      for i, j in pontos.items():
        await ctx.send(str(i) + "->" + str(j))
  if palavra == "rom":
    rom=["Gen I","Gen II","Gen III","Gen IV","Gen V","Gen VI","GenVII"]
    await ctx.send("The winner was " +rom[random.randint(0, (len(rom)-1))])
  if palavra == "random":
    f = open("pokemon.txt", "r")
    pokedex = f.readlines()
    await ctx.send(pokedex[random.randint(0, 718)].replace("\n", ""))
    f.close()

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Espera que a musica acaba ou usa o comando de stop")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Não estou conectado a nenhum vc caralho, deslarga-me.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Se não ta a tocar nada vais parar o que caralho")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Não tens ouvidos caralho, ta a tocar.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
@client.command()
async def link(ctx,palavra : str):
  if palavra == "ESTA":
    embed = discord.Embed(title="Estatistica" , description = "Links/IDs das aulas de ESTA" , color=0x0000ff)
    embed.add_field(name="T" , value = "UCstudent ou [link](https://videoconf-colibri.zoom.us/j/86079979753?pwd=d2pGVU9XWndXVDgyMkc3cnp6NnFDUT09)" , inline=False)
    embed.add_field(name="TP1" , value = "UCstudent 8scl3x" , inline=False)
    embed.add_field(name="TP2" , value = "UCstudent rphefo" , inline=False)
    embed.add_field(name="TP3" , value = "UCstudent npximd" , inline=False)
    embed.add_field(name="TP4" , value = "UCstudent tg0x5r" , inline=False)
    embed.add_field(name="TP5" , value = "UCstudent lgfb07" , inline=False)
    embed.set_footer(text="By Godes")
    await ctx.send(embed = embed)
  elif palavra == "AM2":
    embed = discord.Embed(title="Análise Matemática 2" , description = "Links/IDs das aulas de AM2" , color=0x00ffff)
    embed.add_field(name="T" , value = "UCstudent d8mfpt" , inline=False)
    embed.add_field(name="TP1" , value = "UCstudent 96llxb" , inline=False)
    embed.add_field(name="TP2" , value = "UCstudent 0dzoro" , inline=False)
    embed.add_field(name="TP3" , value = "UCstudent iw6109" , inline=False)
    embed.add_field(name="TP4" , value = "Zoom_id: 829 4928 6293 Passwd 056174" , inline=False)
    embed.add_field(name="TP5" , value = "Zoom_id: 821 1519 7574 Passwd 383912" , inline=False)
    embed.set_footer(text="By Godes")
    await ctx.send(embed = embed)
  elif palavra == "CT":
    embed = discord.Embed(title="Comunicação tecnica" , description = "Links/IDs das aulas de CT" , color=0xff0000)
    embed.add_field(name="T" , value = "[zoom](https://videoconf-colibri.zoom.us/j/83628118958?pwd=clloRmZpbEtSaldCcXhtVWFJRkw4Zz09)" , inline=False)
    embed.add_field(name="P1" , value = "unknown" , inline=False)
    embed.add_field(name="P2" , value = "[zoom](https://videoconf-colibri.zoom.us/j/81306905627?pwd=MVdpeDhjelhYYmlPSURqcmE5Y2ozUT09)" , inline=False)
    embed.add_field(name="P3" , value = "[zoom](https://videoconf-colibri.zoom.us/j/88205239634?pwd=QXZSKytTcHZqTTlxUjlvN0ZLY0RnQT09)" , inline=False)
    embed.add_field(name="P4" , value = "[zoom](https://videoconf-colibri.zoom.us/j/84922018115?pwd=L2p3aEJMZGNKS2xmbUUySkg2emlRdz09)" , inline=False)
    embed.add_field(name="P5" , value = "[zoom](https://videoconf-colibri.zoom.us/j/87265668907?pwd=cDFJcWlVY3owTW4zdDFKOVd5eUkzZz09)" , inline=False)
    embed.set_footer(text="By Godes")
    await ctx.send(embed = embed)
  elif palavra == "PPP":
    embed = discord.Embed(title="Principios de Programacao Procedimental" , description = "Links/IDs das aulas de PPP" , color=0x00ff00)
    embed.add_field(name="TP1" , value = "unknown" , inline=False)
    embed.add_field(name="TP2" , value = "[zoom](https://videoconf-colibri.zoom.us/j/82051168755?pwd=UzdvVWJoS09COVFzZXpWUko2SGxXQT09)" , inline=False)
    embed.add_field(name="TP3" , value = "unknown" , inline=False)
    embed.add_field(name="TP4" , value = "unknown" , inline=False)
    embed.add_field(name="TP5" , value = "[zoom](https://videoconf-colibri.zoom.us/j/83470352559?pwd=RlFuL1lTdVFGb0NuMzBETS9MS0s2Zz09)" , inline=False)
    embed.add_field(name="TP6" , value = "[zoom](https://videoconf-colibri.zoom.us/j/83698940386?pwd=c1Z4NmMyNWtnSWlsZGlYRTlNOVU1dz09)" , inline=False)
    embed.add_field(name="TP7" , value = "[zoom](https://videoconf-colibri.zoom.us/j/87832521332?pwd=bUJkczBUZmpaWkYrWVZBbXRPeUtiZz09)" , inline=False)
    embed.add_field(name="TP8" , value = "[zoom](https://videoconf-colibri.zoom.us/j/82081250603?pwd=RXIwcWx0UzlYRlppZWo1dnl4LzkwZz09)" , inline=False)
    embed.add_field(name="TP9" , value = "unknown" , inline=False)
    embed.add_field(name="TP10" , value = "[zoom](https://videoconf-colibri.zoom.us/j/86925193846?pwd=bEZ2ZGtxU2tZYmcvd0VzV3QrWkhHQT09)" , inline=False)
    embed.add_field(name="videos" , value = "[zoom](https://portal.educast.fccn.pt/videos?c=5604)" , inline=False)
    embed.set_footer(text="By Godes")
    await ctx.send(embed = embed)
  elif palavra== "TFM":
    embed = discord.Embed(title="Topicos de fisica moderna" , description = "Links/IDs das aulas de TFM" , color=0x0000ff)
    embed.add_field(name="T1" , value = "[zoom](https://zoom.us/j/96110162412?pwd=bFNpcS9jNmtmMGJDMENxNWZJUUU4QT09)" , inline=False)
    embed.add_field(name="T2" , value = "[zoom](https://videoconf-colibri.zoom.us/j/84276180632?pwd=a2s4eSs0aHBWanJzT2pnVmpwVmZ3dz09)" , inline=False)
    embed.add_field(name="PL1" , value = "[zoom](https://zoom.us/j/96110162412?pwd=bFNpcS9jNmtmMGJDMENxNWZJUUU4QT09)" , inline=False)
    embed.add_field(name="PL2" , value = "[zoom](https://videoconf-colibri.zoom.us/j/84276180632?pwd=a2s4eSs0aHBWanJzT2pnVmpwVmZ3dz09)" , inline=False)
    embed.add_field(name="PL3" , value = "[zoom](https://zoom.us/j/96110162412?pwd=bFNpcS9jNmtmMGJDMENxNWZJUUU4QT09)" , inline=False)
    embed.add_field(name="PL4" , value = "[zoom](https://videoconf-colibri.zoom.us/j/84276180632?pwd=a2s4eSs0aHBWanJzT2pnVmpwVmZ3dz09)" , inline=False)
    embed.set_footer(text="By Godes")
    await ctx.send(embed = embed)
  elif palavra=="YT":
    embed = discord.Embed(title="Gravacoes de aulas" , description = "Cortesia de Luis Carvalho" , color=0x0000ff)
    embed.add_field(name="Estatistica" , value = "[playlist](https://youtube.com/playlist?list=PLHZfgKGSE-Dp8vJso9Fvenj3SGxSW3BxY)" , inline=False)
    embed.add_field(name="CT" , value = "[playlist](https://youtube.com/playlist?list=PLHZfgKGSE-DpthrToGWr3lFoVMePPuMFF)" , inline=False)
    embed.add_field(name="PPP" , value = "[playlist](https://youtube.com/playlist?list=PLHZfgKGSE-DqdRsCfG7Pwa8yjGyFy3KXm)" , inline=False)
    embed.add_field(name="TFM" , value = "[playlist](https://youtube.com/playlist?list=PLHZfgKGSE-DqnF0fNoYvdbqNr2FVr5-lz)" , inline=False)
    embed.add_field(name="AM2" , value = "[playlist](https://youtube.com/playlist?list=PLHZfgKGSE-DoGYFb3db_XykWK9odO7m6b)" , inline=False)
    embed.set_footer(text="By Godes")
    await ctx.send(embed = embed)
  elif palavra == "help":
    await ctx.send("Para usar o comando escreve .|. links mais a abreviatura do nome da cadeira ou para os links das gravações das aulas YT (AM2,ESTA,CT,PPP,TFM,YT)")
 
@client.command()
async def stream(ctx,palavra:str,link:str):
  canais=[779490839419813921,776100586855596086,813430254601109544]
  for i in range(len(canais)):
    channel = client.get_channel(canais[i])
    await channel.send("Guys o "+palavra+" esta on, venham ver\n"+link);

client.run("Token")
