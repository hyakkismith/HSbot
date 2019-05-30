# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTgzNjc1OTgxNTQ2Mzg5NTA0.XO_1Nw.yJDlcoa78HXA0PNFGnKrie612LU'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

     # !join role_name: role_name役職を得る(特定のチャンネルへ入室する)コマンド
    elif message.content.startswith('!join'):
        reply = f'{message.author.mention} 「!join チーム名」のフォーマットで使ってください。'
        try:
            _, role_name = message.content.split()
        except Exception:
            await message.channel.send(reply)
            return
        role = discord.utils.get(message.guild.roles, name=role_name)
        await message.author.add_roles(role)
        reply2 = f'{message.author.mention} 役職を付与しました。'
        await message.channel.send(reply2)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
