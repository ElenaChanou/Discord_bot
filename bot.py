import discord
import os
from dotenv import load_dotenv
import requests

# 🔹 Load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN not found. Check your .env!")

# 🔹 Meme function
def get_meme():
    try:
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()  # If not JSON, goes to except
        return data.get("url", "Oops! No meme found.")
    except Exception:
        return "Oops! Couldn't fetch a meme."

# 🔹 Create client
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        # Don't respond to its own messages
        if message.author == self.user:
            return

        # $hello command
        if message.content.startswith("$hello"):
            await message.channel.send("Hello World!")

        # $meme command
        elif message.content.startswith("$meme"):
            meme_url = get_meme()
            await message.channel.send(meme_url)

# 🔹 Intents
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# 🔹 Run bot
print("Bot is starting...")  # Shows only a safe message, not the token
client.run(TOKEN)