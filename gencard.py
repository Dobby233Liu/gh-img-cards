#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import json
import requests
import sys

repo = sys.argv[1]
req_json_url = "https://api.github.com/repos/" + repo
api_response = requests.get(req_json_url).content
rep_json = json.loads(api_response)

card = Image.new("RGBA",(730, 301),"white")
cardDraw = ImageDraw.Draw(card)
BigFont = ImageFont.truetype(sys.argv[2], size=35)
SmallFont = ImageFont.truetype(sys.argv[2], size=12)
ghIcon = Image.open(os.path.split(os.path.realpath(__file__))[0]+"ghico.png")
card.paste(ghIcon, (30, 30))
cardDraw.text((120, 30), rep_json['full_name'], font=BigFont, fill="black")
cardDraw.text((250, 10), "repo created " + rep_json['created_at'], font=SmallFont, fill="grey")
cardDraw.text((120, 100), rep_json['description'], font=SmallFont, fill="black")
card.save(sys.argv[3])
