import requests
import json


class DiscordAPI:
    def __init__(self, webhook):
        self.__webhook = webhook

    def __create_message(self, message):
        return {
          "embeds": [{
            "author": {
              "name": message['author_name'],
              "icon_url": message['author_icon']
            },
            "color": 15258703, #TODO: Add as a input
            "fields": [
              {
                "name": "Commit",
                "value": message['from_branch'],
                "inline": 'true'
              },
              {
                "name": "Branch",
                "value": message['to_branch'],
                "inline": 'true'
              },
              {
                "name": message['pr_link'],
                "value": f":point_up_2: {message['pr_title']} :point_up_2:"
              },
              {
                "name": f"{message['author_name']} commited",
                "value": "@here Please Review the PR :raised_hands:!!!"
              }
            ],
            "footer": {
              "text": f"Created at {message['pr_date']}"
            }
          }]
        }

    def post_message(self, message):
        headers = {
            "Content-Type": "application/json"
        }
        embeds = self.__create_message(message=message)
        return requests.post(url=self.__webhook, headers=headers, data=json.dumps(embeds))
