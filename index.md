<h1>BlockyBot - Rewritten in Python</h1>

I've decided to rewrite my discord bot, blockybot in python because:

The hosting provider i was using allowed me to create custom commands, embeds, etc, but the uptime was terrible, and i couldn't stand it.
I had to watch an AD every 30 miniutes to keep in online (like, come on)
Literally 0 support, like if it broke, they couldn't care less if they tried.

So im rewriting in in python. Anyone can use this as a template to make their own discord bot, if they would like, but you will need to add your OWN discord bot token in the .env file.

<h1>Required Packages</h1>

These are the **required** packages to run this bot.

discord.py - to interface with discord and use their api
To install, you can use pip:

Python 3.5+ Windows:

`py -3 -m pip install -U discord.py`

Python 3.5+ Mac/Linux:

`python3 -m pip install -U discord.py`

python-dotenv
Required to interface with the .env file so if more files are added, a token will not be necesarry in all files, only the .env file.
To install, you can also use pip.

Python 3.5+ Global:

`pip install -U python-dotenv`

