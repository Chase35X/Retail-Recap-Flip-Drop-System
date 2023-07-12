import numbers
from os import name
from tracemalloc import start
from types import resolve_bases
from dhooks import embed
import discord
import dhooks
from dhooks import Webhook, Embed, File
from io import BytesIO
from discord import webhook
from discord.audit_logs import AuditLogDiff
from discord.raw_models import RawReactionClearEmojiEvent
import requests



allhooks = [
            # Input list of webhooks
            ]



title = # Input title of product
prodInfo = # Input information on product
prices = # Input retail and resell prices of product
timeAndDate = # Input time and date of product drop (release)
dropImage = # Input a link of product
links = # Input any useful links you want to include in the embed


def main():
    embed = Embed(
        title=title,
        description = "",
        color = 0xADD8E6
    )

    embed.add_field(name=":shopping_bags: Product Info", value=prodInfo, inline=False)
    embed.add_field(name=":1234: Numbers", value=prices, inline=False)
    embed.add_field(name=":alarm_clock: Time/Date", value=timeAndDate, inline=False)
    embed.add_field(name=":link: Links", value=links, inline=False)
    embed.set_image(url=dropImage)
    embed.set_author(name="Chase35X ~ Retail Recap")
    embed.set_footer(text="DM Chase35X#1234 with questions | Good luck! | Have a good day")

    with open(r' # Input desktop location of image for embed, 'rb') as f:
        img = f.read()

    for webhook in allhooks:
        webhook.get_info()
        webhook.modify(name='Retail Recap', avatar=img)
        try:
            webhook.send(embed=embed)
        except:
            print(webhook + " didnt work")




main()
