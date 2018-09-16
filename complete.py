import wx
from chatterbot import ChatBot
import wikipedia
#import Google as search
#from espeak import espeak
#import pyttsx
'''import wolframalpha
import speech_recognition as sr

app_id = "2E9EPV-L2X8EXKWJE"
client = wolframalpha.Client(app_id)
'''
chatbot = ChatBot('Run Obvious', trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer')

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Voicebot")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am VoiceBot. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

        input = self.txt.GetValue()
        input = input.lower()
        '''if input == " ":
            r = sr.Recognizer()
            with sr.Microphone() as source:
                    audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google; {0}".format(e))
'''
        try:
            print(chatbot.get_response(input))
        except:
            try:
                input = input.split(' ')
                input = ' '.join(input[2:])
                print (wikipedia.summary(input))
            except:
                try:
                    for answer in search(input, tld ='co.in', num=5, stop=1, pause=2):
                        print(answer)
                except:
                    try :
                        google.search("https://www.google.co.in/#q=" + input, num=5, stop=2)
                    except:
                        print("idk")


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
