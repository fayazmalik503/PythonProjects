from instabot import Bot

'''You can follow anyone'''
bot = Bot()
Bot.login(username = "xyz@gmail.com", "password")
bot.follow('AnyPersonThatYouWantToFollow')

'''You can also unfollow anyone'''
bot.unfollow('AnyPersonThatYouWantToFollow')

'''You can also upload'''
bot.upload_photo("Path_of_the_File.jpeg", caption = "any title with image you want to share")

'''You can also send person message'''
bot.send_message("your message,['first person', 'second person'])