from dotenv import load_dotenv
import discord
import os
import asyncio
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print("=====DISCORD CONECTADO======\nID: ", self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None
        for text in ['!r']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command == '!r':
            try:
                bot_response = chatgpt_response(prompt=user_message)
                if len(bot_response) > 1500:
                    bot_response = bot_response[:1500]
                    await message.channel.send(f"Limite máximo de caracteres excedido. A resposta gerada foi:\n {bot_response}")
                else:
                    await message.channel.send(f"{bot_response}")
            except Exception as e:
                print(f"Ocorreu um erro")
                await message.channel.send("Ocorreu um erro ao processar sua mensagem. Por favor, tente novamente mais tarde.")
                await self.run_discord_bot()

    async def run_discord_bot(self):
        from run import run_discord_bot
        await run_discord_bot()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


