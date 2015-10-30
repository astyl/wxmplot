
import wx

class AbcMenuBar(wx.MenuBar):
    def __init__(self,parent,menusCfg):
        self.parent = parent
        wx.MenuBar.__init__(self)
        for menuCfg in menusCfg:
            self.appendMenu(menuCfg)
            
    def appendMenu(self,menuCfg):
        label = menuCfg["label"]
        items = menuCfg["items"]
        menu = wx.Menu()
        for menuItemCfg in items:
            self.appendMenuItem(menuItemCfg,menu)
        self.Append(menu,label)
    
    def appendMenuItem(self,menuItemCfg,menu):
        if menuItemCfg == "--":
            menu.AppendSeparator()
        else:
            m_id = wx.NewId()
            text = menuItemCfg["label"]
            handler = menuItemCfg["handler"]
            menu.Append(m_id,text)
            handlerFn = getattr(self.parent,handler)
            self.Bind(wx.EVT_MENU, handlerFn, id = m_id)

if __name__ == "__main__":
    app = wx.App()
    class FrameC(wx.Frame):
        def cbMenuItem1(self,event):
            print event
        def cbMenuItem2(self,event):
            print event
    fr = FrameC(None)
    menusCfg = [
        { 
            "label":"menu1",
            "items": [
                {
                    "label":"menuItem1",
                    "handler": "cbMenuItem1"
                },
                "--",
                {
                    "label":"menuItem2",
                    "handler": "cbMenuItem2"
                },
            ]          
        },
    ]
    fr.SetMenuBar(AbcMenuBar(fr,menusCfg))
    fr.Show()
    app.MainLoop()
