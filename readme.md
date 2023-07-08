
# Quanta Events Bot

Quanta Events Bot is a versatile Discord bot developed using the Nextcord library. It provides several features and commands to enhance your Discord server experience.

## Features

- Set up a global channel for event announcements using `!setupglobalchannel` command.
- Share event details to the global channel with the `!shareevent` command.
- Get a list of available commands using the `!help` command.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/quanta-events-bot.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Replace `YOUR_BOT_TOKEN` in the main bot file (`main.py`) with your actual bot token.

4. Run the bot:

   ```shell
   python main.py
   ```

## Usage

1. Invite the bot to your Discord server using the following URL:

   ```
   https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=YOUR_PERMISSIONS
   ```

   Replace `YOUR_CLIENT_ID` with your bot's client ID and `YOUR_PERMISSIONS` with the necessary bot permissions. Adjust the permissions based on the features your bot requires.

2. Set up a global channel for event announcements by using the `!setupglobalchannel` command in any server channel with administrator permissions.

3. Share event details to the global channel using the `!shareevent` command in the server channel where the event details should be sent.

4. To see the list of available commands, use the `!help` command.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
Thanks for Reading!
