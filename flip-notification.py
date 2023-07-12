from turtle import title
from types import resolve_bases
import discord
import dhooks
from dhooks import Webhook, Embed, File
from io import BytesIO
from discord import webhook
import requests

webhooks = [
            # Input list of webhooks here
            ]



##FLIP INFO##
productName = '' # Input product name

description = "" # Input useful information and description of flip

image = '' # Input link of image 

def main(color, footer, logo, webhook, cg):
    embed = Embed(
        color = color,
        description = description
    )

    embed.set_title(title=str(productName))
    embed.set_author(name=cg + " | Retail Recap")
    embed.set_footer(text= footer)
    embed.set_image(url=image)

    webhook.get_info()
    webhook.modify(name=cg, avatar = logo)
    webhook.send(embed=embed)



for hook in webhooks:
    with open(r' # location of image file, 'rb') as f:
        img = f.read()
    main(0xADD8E6, "Contact Chase35X#1234 for more info!", img, hook, "Chase35X")


main()
