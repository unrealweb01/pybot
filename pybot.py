import requests
from telegram_tools import TelegramResponse
class Bot:
    def __init__(self,token):
        self.token=token
        self.update=self.getupdate()
    def getupdate(self):
        res=requests.get(f"https://api.telegram.org/bot{self.token}/getUpdates")
        updates=res.json()
        updates["result"]=updates["result"][0]
        return TelegramResponse.parse_obj(updates)
    def sendMessage(self,text):
        chat_id=self.update.result.message.chat.id
        res=requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage",params={"chat_id":chat_id,"text":text})
        return res.json()
    def setWebhook(self,url):
        res=requests.post(f"https://api.telegram.org/bot{self.token}/setWebhook?url={url}")
        return res.json()
    def deleteWebhook(self):
        res=requests.post(f"https://api.telegram.org/bot{self.token}/setWebhook?remove")
        return res.json()
##bot_token="6640559959:AAElVoUIZZ-TBXUFpHgG2e7hVNmz33qsQnc"
##bot=Bot(bot_token)
