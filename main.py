from pyrubi import Bot
from datetime import datetime
from threading import Thread
from time import sleep

# Rubika : @Persian_Python, @Pyrubika, @Pyrubi_Example

#------------------
# شناسه اکانت
auth = 'iufidjgjlosdajkjkfo4esgqzgr'
# لینک پست
post_link = 'https://rubika.ir/Persian_PyThon/DDBEJAHJDBCBAFE'
# زمان استراحت هربار ارسال (ثانیه)
speed_send = 0.5
#------------------

bot = Bot(auth)
post_info = bot.get_link_info(post_link)
count_send = 0

def forward_post(chat_id, more_info):
    try:
        chat_title = more_info["abs_object"].get("title", more_info["abs_object"].get("first_name", more_info["abs_object"].get("last_name", "None")))
        time_send = datetime.now().strftime('%H : %M : %S - %p')
        if 'SendMessages' in more_info['access']:
            forward_info = bot.forward_message(post_info['object_guid'], [post_info['message_id']], chat_id)
            return print('\u001b[37m' + str(count_send) + '\u001b[35m' + ' - Sended to the ' + '\u001b[36m' + chat_title + '\u001b[34m' + f'\nChat id : {chat_id}' + '\u001b[33m' + f'\nCount seen : {forward_info["message_updates"][0]["message"]["count_seen"]}' + '\u001b[32m' + f'\nTime send : {time_send}\n')
        print('\u001b[31m' + f'The {chat_title} is locked and cannot be sent !')
    except:
        pass

while True:
    try:
        print('\u001b[33m' + 'Getting chats ...')
        chats = bot.get_chats()['chats']
        print('\u001b[32m' + 'Count chats : ' + '\u001b[36m' + str(len(chats)) + '\n')
        for chat in chats:
            chat_id = chat['object_guid']
            if chat_id.startswith('u0') or chat_id.startswith('g0'):
                count_send += 1
                Thread(target=forward_post, args=[chat_id, chat]).start()
                sleep(speed_send)
    except:
        continue