# Telegram-bot :robot:
Bot moderator for telegram chat. Will be improved.

## Installation :gear:
If you are cloning a project, run it first, otherwise you can download the source on the release page and skip this step.

    git clone https://github.com/White-prince/Moderbot.git
    
You will need to install the libraries before starting the assistant

    pip install aiogram
    
You will also need a token to run your bot

## Usege :information_source:
After installing all the necessary libraries and files, you need to go to telegram and find the bot father - @BotFather. Create a bot and get its token and enter it in the config.py.

    TOKEN = ''

Also get the ID of the group where you will add the bot - @username_to_id_bot. Enter in id group.

    GROUP_ID = ()

Write the command in the terminal:

    python main.py

About the code:
- The folder messages.py contains prepared messages
- The folder keyboards.py contains the speed dial functions
- The folder filters.py contains the administrator authentication function
