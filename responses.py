import random

def handleResponse(message) -> str:

    if message.lower() == 'hello':
        return 'Hello there'

    if message == 'roll':
        return str(random.randint(1,6))

    if message == '!help':
        return "`This is a help message that you can modify.`"

def pushResponse(message):
    print('push response')


def main():
    print('Hello there')

if __name__=='__main__':
    main()
