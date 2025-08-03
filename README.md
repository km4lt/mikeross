# Mike Ross

**Mike Ross** is a Discord bot powered by Google Gemini. It impersonates a sharp, polite, and witty assistant who replies concisely—just like the fictional legal prodigy. Mention it, reply to it, or use `!ask` to get short, to-the-point answers.

## Goal

The bot was built to explore LLM-driven Discord automation using Google Gemini’s `generate_content` API, while enforcing short-form, high-value replies with a bit of character.

## Features

- Gemini 2.0 Flash-powered text generation
- Persona-driven, concise responses (100 words max)
- Three trigger modes:
  - Mentioning the bot
  - Replying to the bot
  - Using `!ask` command
- Typing indicator while generating
- Long replies are chunked and sent in multiple messages

## Example Usage

**Mention**:
```
@Mike Ross How do I learn Python fast?
```

**Command**:
```
!ask What's a good project for beginners?
```

**Reply to Bot**:
Reply to a previous message from the bot with a follow-up prompt.

## Environment Variables

Set the following in your `.env` or directly in the script:

```python
DISCORD_BOT_TOKEN = "your_discord_token_here"
GEMINI_API_KEY = "your_gemini_api_key_here"
```

## Libraries Used

- `discord.py` — For Discord event handling  
- `google.generativeai` — To access Gemini models

## Installation

1. Ensure Python 3.8+ is installed  
2. Install dependencies:

    ```bash
    pip install discord.py google-generativeai
    ```

3. Run the bot:

    ```bash
    python bot.py
    ```
