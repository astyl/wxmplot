import wx
from wx.py.shell import Shell

class ShellDialog(wx.Dialog):
    """ Python shell terminal """
    def __init__(self,*args,**kwargs):
        wx.Dialog.__init__(self,*args,**kwargs)
        self.__shell = Shell(self)
        
    def update_locals(self,**dlocals):
        self.__shell.interp.locals.update(dlocals)

if __name__ == "__main__":
    app=wx.App()
    frame = wx.Frame(None)
    app.SetTopWindow(frame)
    sc=ShellDialog(frame,size=(500,300))
    frame.Show()
    sc.Show()
    sc.update_locals(mul=lambda x,y: x*y,
                       var1 = "variable 1")
    app.MainLoop()