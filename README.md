# Advanced Telegram Forward Bot

Welcome to the Advanced Telegram Forward Bot repository! This Telegram bot is designed to provide powerful and advanced message forwarding capabilities.

## Features

- Forward messages from various sources (channels, groups, users, bots) to different destinations.
- Two forwarding methods: through a dummy bot and through a userbot.
- Customizable caption and buttons for forwarded messages.
- Support for restricted chats and permissions.
- Skip duplicate messages.
- Filter messages based on type, extensions, and keywords.

## Getting Started

To use this bot, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` using `pip`.
3. Create a `config.py` file and add your bot token and other configuration details (see `config_template.py` for reference).
4. Create a MongoDB database and provide the database URL in `config.py` for de-duplication.
5. Set up your userbot if you're using the userbot forwarding method (see `userbot.py`).
6. Add your dummy bot tokens to `dummybot_tokens.py` (if using the dummy bot method).
7. Run `bot.py` to start your Telegram bot.

## Usage

Once your bot is up and running, you can interact with it through Telegram. Here are some available commands:

- `/start`: Check if the bot is alive.
- `/forward`: Forward messages.
- `/private_forward`: Forward messages from private chats.
- `/unequify`: Delete duplicate media messages in chats.
- `/settings`: Configure your bot's settings.
- `/stop`: Stop ongoing tasks.
- `/reset`: Reset your bot's settings.

For more detailed information and examples, check the [Help](#help) section below.

## Help

To get more information about how to use the bot and its features, you can use the `/help` command, which provides detailed guidance on available commands, settings, and more.

## Support and Updates

For support and updates, join our [Support Group](#) and [Update Channel](#).

## Donate

If you find this bot helpful and would like to support its development, consider making a donation to the developer:

UPI ID: `krishna527062@oksbi`

## About

- **Bot:** Advanced Telegram Forward Bot
- **Creator:** Your Name
- **Hosted On:** Hosting Service
- **Language:** Python 3
- **Library:** Pyrogram, asyncio 2.0.0
- **Version:** 1.0.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
