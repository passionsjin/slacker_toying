import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
from config.keys import teams_url

myTeamsMessage = pymsteams.connectorcard(teams_url)

# Add text to the message.
myTeamsMessage.text("this is my text")

# send the message.
myTeamsMessage.send()