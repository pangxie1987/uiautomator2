'''
微信包itchat
'''
import itchat

from itchat.content import TEXT


# @itchat.msg_register

# def simple_reply(msg):

#   if msg['Type'] == TEXT:

#     return 'I received: %s' % msg['Content']

# itchat.auto_login()

# itchat.run()

itchat.login()

friends = itchat.get_friends(update=True)[0:]
print(friends)
itchat.run()
