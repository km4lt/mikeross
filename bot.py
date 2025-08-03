import discord
from google import genai

DISCORD_BOT_TOKEN = ''
GEMINI_API_KEY = ''


client_gemini = genai.Client(api_key=GEMINI_API_KEY)


intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# Mike Ross persona
MIKE_ROSS_PERSONA = (
    "You're a polite, sharp and witty AI bot made to help users Answer in 100 words max.\n\n"
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    is_mentioned = bot.user.mentioned_in(message)
    starts_with_command = message.content.lower().startswith('!ask')

    is_reply_to_bot = (
        message.reference and message.reference.resolved
        and message.reference.resolved.author == bot.user
    )

    if is_mentioned or starts_with_command or is_reply_to_bot:
        prompt = message.content.strip()

        if is_mentioned:
            prompt = prompt.replace(f'<@{bot.user.id}>', '').strip()
        elif starts_with_command:
            prompt = prompt[len('!ask'):].strip()

        if not prompt:
            await message.channel.send("Give me something to work with, genius. Type a prompt.")
            return

        full_prompt = MIKE_ROSS_PERSONA + prompt
        print(f"[Prompt] {prompt}")

        try:
            async with message.channel.typing():
                response = client_gemini.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=full_prompt
                )
                output = response.text.strip()

                if len(output) <= 2000:
                    await message.reply(output)
                else:
                    # Reply with first 2000 chars
                    await message.reply(output[:2000])
                    # Send remaining output in chunks without replying
                    for i in range(2000, len(output), 2000):
                        await message.channel.send(output[i:i+2000])

        except Exception as e:
            print(f"Error: {e}")
            await message.reply(f"Error: {e}")

if __name__ == '__main__':
    bot.run(DISCORD_BOT_TOKEN)

