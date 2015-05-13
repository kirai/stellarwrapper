import wx
import requests
import json

URL = 'https://test.stellar.org:9002'
ACCOUNT_ADDRESS = ''

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    # Retrieves the balance from a account_info json response data
    def get_account_balance(pum):
        balance = json.loads(pum.text)
        return balance['result']['account_data']['Balance']

    def InitUI(self):    
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.SetSize((600, 400))
        self.SetTitle('Future Coins')
        self.png = wx.StaticBitmap(self, -1, wx.Bitmap("future.png", wx.BITMAP_TYPE_ANY))


        self.lblname = wx.StaticText(self, label="You have :", pos=(150,200))
        self.lblname = wx.StaticText(self, label="You have :", pos=(150,200))
        

        # Getting account information
        payload = { 'method' : 'account_info',
                    'params': [{'account': ACCOUNT_ADDRESS }]
                  }
        pum = requests.post(URL, data= json.dumps(payload))
        balance = json.loads(pum.text)
        balance = balance['result']['account_data']['Balance']
        self.lblname = wx.StaticText(self, label=balance, pos=(250, 200))

        self.Centre()
        self.Show(True)
        

    def OnQuit(self, e):
        self.Close()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()