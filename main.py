import os

import bot


def main():
    print('!')
    token = os.getenv('TOKEN')
    print(token)
    #bot.runDiscordBot(os.getenv('TOKEN'))

if __name__=='__main__':
    main()
