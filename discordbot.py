import discord
from discord.ext import tasks
from datetime import datetime
 
TOKEN = "自分のサーバー"
client = discord.Client()
CHANNEL_ID = 自分のサーバー

A = []
 
#bot起動完了時に実行される処理
@client.event
async def on_ready():
    print('ログイン成功')
 
#メッセージ受信時に実行される処理
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if message.content.startswith('/test'):
        await message.channel.send('稼働中')
#memo
    if message.content.startswith('kk'):
        await message.channel.send(A)
    if message.content.startswith('/memo'):
        list = ""
        for i in A:
            list += i
            list += '\n'
        await message.channel.send(list)
    if message.content.startswith('/add'):
        await message.channel.send("memoを入力してください")
        add = await client.wait_for("message")
        await message.channel.send("確認しました")
        A.append(add.content)
    if message.content.startswith('/del'):
        await message.channel.send("消したいmemoを入力してください")
        de = await client.wait_for("message")
        d = de.content
        for i in A:
            if i == d:
                await message.channel.send("削除しました")
                A.remove(d)
            else:
                await message.channel.send("ないです")


client.run(TOKEN)