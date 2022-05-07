import requests
import time
import telebot

# bot=telebot.TeleBot('5149745229:AAFau6dU0uG5K34OeSbwQ8jvBi0eItfiVYU')


url="https://api.telegram.org/bot{5149745229:AAFau6dU0uG5K34OeSbwQ8jvBi0eItfiVYU}/sendMessage?chat_id={chat_id}&text={hii}"
para={"chat_id" : "918229363",
      "photo" : "detectedface/faces.jpg",
      "caption" : time.time()}
rep=requests.post(url,data=para)
print(rep.text)
#
# bot.send_photo('918229363',photo=open('detectedface/faces.jpg'))

# url = 'https://api.telegram.org/bot5149745229:AAFau6dU0uG5K34OeSbwQ8jvBi0eItfiVYU/sendPhoto?chat_id=918229363'
# files = {'file':open('detectedface/faces.jpg', 'rb')}
# requests.post(url, files=files)