# Work with Python 3.6
import discord
from db import post_search_data, fetch_search_data
import settings as my_settings
from search import search_main

TOKEN = my_settings.DISCORD_TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('hi'):
        msg = 'Hey {}'.format(message.author.mention)
        await message.channel.send(msg)

    elif message.content.startswith('!google'):
        query = message.content.split(None, 1)
        if len(query)<2:
            print('Nothing to google')
            return
        else:
            query = query[1]
        author_id = message.author.id
        post_search_data(author_id, query)

        results = search_main(query)
        if results:
            links = ' \n'.join(results)
            # print(links)
            msg = 'Hey {}, you searched for "{}". The top five results are: \n {}'.format(
                message.author.mention, query, links)
        else:
            msg = 'Hey {}, you searched for "{}". \n Sorry, no matching links found.'.format(
                message.author.mention, query)
        await message.channel.send(msg)

    elif message.content.startswith('!recent'):
        query = message.content.split(None, 1)
        if len(query)<2:
            query = ''
        else:
            query = query[1]
        author_id = message.author.id
        results = fetch_search_data(author_id, query)
        # print(results)
        keywords = 'Hey {}, '.format(message.author.mention)
        if(len(results) > 0):
            keywords += 'your matching search results are: \n' + \
                ' \n'.join([x[1] for x in results])
        else:
            keywords += 'Sorry.. No matching results found'
        await message.channel.send(keywords)


@client.event
async def on_ready():
    print('Logged in as Bot :',client.user.name)
    print()

client.run(my_settings.DISCORD_TOKEN)
