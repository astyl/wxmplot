# -*-coding:Utf-8 -*

import wx
from wx.py.shell import Shell

class ShellCtrl(Shell):
    """ Python shell terminal.
    To add python objects are, use the method 'updtShellLocals'    
    """
    def updtShellLocals(self,**dlocals):
        self.interp.locals.update(dlocals)

if __name__ == "__main__":
    app=wx.App()
    frame = wx.Frame(None)
    sc=ShellCtrl(frame)
    frame.Show()
    app.MainLoop()