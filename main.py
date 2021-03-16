import discord
import os
import time


class MyClient(discord.Client):
  async def on_ready(self):
    print("Logged in as {0.user}".format(client))


  async def on_message(self, message):
    if message.author == client.user:
      return
  
    if message.content.startswith("&hello"):
      await message.reply("OOOH OOH Ah! Hello {0.user}".format(client), )
    

    if message.content.startswith("&league"):
      await message.channel.send("OOOH OOH Ah!")
      time.sleep(0.5)
      await message.channel.send("WEEEE OOOOH WEEEE OOOOH!")
      time.sleep(0.1)
      await message.channel.send("Attention all @apes")
      time.sleep(0.1)
      await message.channel.send("LEAGUE NOW! ITS A GREAT GAME!")


    if message.content.startswith("&bloons"):
      await message.channel.send("OOOH OOH Ah!")
      time.sleep(0.5)
      await message.channel.send("Any @apes, that are also Bloonsers?!")



client = MyClient()




client.run(os.getenv("TOKEN"))