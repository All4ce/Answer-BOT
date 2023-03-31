from app.discord_bot.discord_api import client, discord_token

def run_discord_bot():
    client.run(discord_token)

if __name__ == '__main__':
    run_discord_bot()
