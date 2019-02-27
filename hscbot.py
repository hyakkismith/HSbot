import logging
import discord  # インストールした discord.py
import csv
import asyncio
import random
import random, string # ランダム文字列



logging.basicConfig(level=logging.INFO) # エラーを出力する
client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    print('ログインしました')
    



@client.event
async def on_message(message):

    #メッセージがbotのものであった場合、無視
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    # !mksc secret_channel_name allowed_role: allowed_role役職のみが見れるsecret_channel_nameチャンネルを作るコマンド。
    if message.content.startswith('!mksc'):
        try:
            _, channel_name, allow_role_name = message.content.split()
        except Exception:
            await client.send_message(message.channel, "「!mksc 作るチャンネル名 許可するロール名」のフォーマットで使ってください。")
            return
        allowed_role = discord.utils.get(message.server.roles, name=allow_role_name)
        everyone = discord.PermissionOverwrite(read_messages=False)
        visible_role = discord.PermissionOverwrite(read_messages=True)
        await client.create_channel(message.server, channel_name, (message.server.default_role, everyone), (allowed_role, visible_role))
        await client.create_channel(message.server, channel_name, (message.server.default_role, everyone),
                                    (allowed_role, visible_role), type=discord.ChannelType.voice)
        await client.send_message(message.channel, "チャンネルを作成しました。")

    # !mkr role_name: role_name役職を作るコマンド。
    elif message.content.startswith('!mkr'):
        try:
            _, role_name = message.content.split()
        except Exception:
            await client.send_message(message.channel, "「!mkr ロール名」のフォーマットで使ってください。")
            return
        await client.create_role(message.server, name=role_name)
        await client.send_message(message.channel, "役職を作成しました。")

    # !join role_name: role_name役職を得る(特定のチャンネルへ入室する)コマンド
    elif message.content.startswith('!join'):
        try:
            _, role_name = message.content.split("")
        except Exception:
            await client.send_message(message.channel, "「!join チーム名」のフォーマットで使ってください。")
            return
        role = discord.utils.get(message.server.roles, name=role_name)
        await client.add_roles(message.author, role)
        await client.send_message(message.channel, "役職を付与しました。")

    # CSVファイルからいっぺんに作っちゃえ！
    elif message.content.startswith('!mkcsv'):

        # ファイル読み込み
        csv_file = open("i:\pythonstudy\discordbot\contestant_list.csv", "r", encoding="utf_8", errors="", newline="")
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"',
                       skipinitialspace=True)
        c_list = next(f)
        print(c_list)

        for c_name in c_list:

            try:
                # _, channel_name = message.content.split()
                channel_name = c_name
            except Exception:
                await client.send_message(message.channel, "「!mkcsv」のフォーマットで使ってください。")
                return

            # 役職
            await client.create_role(message.server, name=channel_name)
            await client.send_message(message.channel, "役職を作成しました。")

            # チャンネル
            allowed_role = discord.utils.get(message.server.roles, name=channel_name)
            everyone = discord.PermissionOverwrite(read_messages=False)
            visible_role = discord.PermissionOverwrite(read_messages=True)
            await client.create_channel(message.server, channel_name, (message.server.default_role, everyone), (allowed_role, visible_role))
            await client.create_channel(message.server, channel_name, (message.server.default_role, everyone),
                                        (allowed_role, visible_role), type=discord.ChannelType.voice)
            await client.send_message(message.channel, "チャンネルを作成しました。")

    # いっぺんに作っちゃえ！
    elif message.content.startswith('!mk'):
        try:
            _, channel_name = message.content.split()
        except Exception:
            await client.send_message(message.channel, "「!mk 作るチャンネル名ロール名」のフォーマットで使ってください。")
            return

        # 役職
        await client.create_role(message.server, name=channel_name)
        await client.send_message(message.channel, "役職を作成しました。")

        # チャンネル
        allowed_role = discord.utils.get(message.server.roles, name=channel_name)
        everyone = discord.PermissionOverwrite(read_messages=False)
        visible_role = discord.PermissionOverwrite(read_messages=True)
        await client.create_channel(message.server, channel_name, (message.server.default_role, everyone), (allowed_role, visible_role))
        await client.create_channel(message.server, channel_name, (message.server.default_role, everyone),
                                    (allowed_role, visible_role), type=discord.ChannelType.voice)
        await client.send_message(message.channel, "チャンネルを作成しました。")
client.run("NTM0NzQ3ODcxMjkyMTYyMDQ5.DyC3Xg.66jhlD4NbRnsGyitQAg8R8NRZp0")