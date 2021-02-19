import discord
import random
import os
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def musicas(a):
    if a[0:5] == "bocas":
        nome = a[6:]
        a = str(random.randint(0, 4))
    dic = {
        "hino lei":
        "É ferro, é aço, é merda ao calhamaço\nInformatica marca o passo\nQuem foi? Quem viu?P´rá puta que os pariu\nEu bem dizia que era grossa e não cabia\nEra a maior de toda a academia\nPassou passou passou passou passou ao lado\nTenham cuidado senão são enrabados\nEu bem te disse que ela era pneumática\nA maior piça é a piça de **informática**",
        "atirei o pau a gata":
        "Atirei o pau à gata ta Mas a gata ta\nMas a gata ta,não mordeu eu eu\n Oh minha puta ta,\nPõe-te de quatro tro\nQue já vais ver o que é foder com um informático!\nEla fez-me um cafoné né né\nE mesmo assim sim sim, ficou de pé pé pé\nOh minha puta ta,`tra vez de quatro tro,\nQue vais levar mais uma vez com um informático",
        "hino polo ii":
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


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.|. cona'):
        await message.channel.send('https://gph.is/g/ZkVLMrp')
    elif message.content == "meixedo":
        await message.channel.send("meixedo? esse gajo é alta gay")
    elif message.content == "santi":
        await message.channel.send("Passou a IPRP nem sabe como, mas tb vai pra DESIGNÉ pro ano")
    elif message.content == "machado":
        await message.channel.send("Esse gajo um dia ainda vai acabar com o stock de erva de coimbra")
    elif message.content == "moreira":
        await message.channel.send("Plat no lol carregado")
    elif message.content == "soveral":
        await message.channel.send("Noites magicas")
    elif message.content == "carvalho":
        await message.channel.send("Weeb do caralho, quando ele fuder com uma gaja o mundo acaba!!!")
    elif message.content == "hugo":
        await message.channel.send("Não era esse gajo que tinha crush na stora de ESTA?")
    elif message.content.startswith(".|. pokemon"):
        pontos = {
            "Bernas": 1,
            "Folhas": 0,
            "Carvalho": 0,
            "Vasques": 1,
            "Alves": 0,
            "Pino": 0,
            "Martim": 0,
        }
        if message.content[12:] == "rom":
            roms = [
                "Gen I", "Gen II", "Gen III", "Gen IV", "Gen V", "Gen VI",
                "GenVII"
            ]
            await message.channel.send("The winner was " +
                                       roms[random.randint(0, len(roms))])
        if message.content[12:18] == "random":
            f = open("pokemon.txt", "r")
            pokedex = f.readlines()
            await message.channel.send(pokedex[random.randint(0, 718)].replace(
                "\n", ""))
            f.close()
        if message.content[12:] == "leaderbord":
            for i, j in pontos.items():
                await message.channel.send(str(i) + "->" + str(j))
    elif message.content.startswith(".|. musica"):
        if message.content == '.|. musica':
            await message.channel.send(
                "Escolhe uma: Hino LEI | Atirei o pau a gata | Hino Polo II | BOCAS"
            )
        else:
            try:
                await message.channel.send(
                    musicas(message.content[11:].lower()))
            except:
                await message.channel.send("A musica não existe")



client.run("Token")
