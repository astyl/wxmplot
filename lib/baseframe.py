
import wx
from basepanel import BasePanel
from abcmenubar import AbcMenuBar 
from shelldialog import ShellDialog

class BaseFrame(wx.Frame):
    """ 
    BaseFrame is a wx.Frame meant to be the top window application.
    
    It is delivered with :
    - panels management : 
        It can hold several panels.
        Each panel holds a matplotlib.figure        
    
    - menu & short-cuts management :
        configuration with a dictionnary (automatic binding, etc..)
    
    - python shell console :
        To interact with the figure
    """
    panelIds = [wx.NewId()] # baseFrame has at least one basePanel
    basePanelClasses = [BasePanel]
    # menus 
    menusCfg = [
        { 
            "label":"file",
            "items": [
                "--",
                {
                    "label":"Exit",
                    "handler": "on_exit"
                },
            ],      
        },
        { 
            "label":"help",
            "items": [
                "--",
                {
                    "label":"shell",
                    "handler": "on_shell"
                },
            ]         
        },                
    ]
    menuClass = AbcMenuBar
    # 'shortcutCfg' configure the short-cuts to bind on the panel 
    #    Example :
    #        shortcutCfg = [ (wx.ACCEL_ALT, ord('X'), "onAltX"), ]
    #        with "onAltX" the callback method name
    shortcutCfg = []    
    
    def __init__(self,parent,**kwargs):
        """ Constructor
        wx.Frame arguments
        """
        kwargs["title"] = kwargs.get("title","wxmplot")
        kwargs["size"] = kwargs.get("size",(800,600))
        wx.Frame.__init__(self, parent, **kwargs)
        
        # multi-panels
        self.panels = {}
        for panelClass,panelId in zip(self.basePanelClasses,self.panelIds):
            self.panels[panelId] = panelClass(self,id=panelId)
    
        # short_cuts to bind
        self._set_shortcuts()
        
        # menus
        menu = self.menuClass(self,self.menusCfg)
        self.SetMenuBar(menu)
        
        # ShellCtrl
        self._shellDialog = ShellDialog(self,size=(400,300),title="shell")
        self.update_shell_locals()
        
    def get_canvas(self,panelId = None):
        """ return the matplotlib canvas of the panel """
        if panelId is None:
            panelId = self.panelIds[0]
        return self.panels[panelId].get_canvas()
    
    def get_figure(self,panelId = None):
        """ return the matplotlib canvas of the figure """
        if panelId is None:
            panelId = self.panelIds[0]
        return self.panels[panelId].get_figure()
    
    def update_shell_locals(self):
        self._shellDialog.update_locals(**self.get_shell_locals())
        
    def get_shell_locals(self):
        shellLocals = {
            "frame": None,
            "panels": self.panels,
            "panelsId": self.panelIds,
            "figures": [self.get_figure(panelId) for panelId in self.panelIds],
        }
        return shellLocals
        
    def draw(self, panelId = None):
        """ draw on the panel """
        if panelId is None:
            panelIds = [self.panelIds[0]]
        else:
            panelIds = self.panelIds
        for panelId in panelIds:
            self.panels[panelId].draw()

    def _set_shortcuts(self):
        """ """
        table = []
        for key1,key2,methodName in self.shortcutCfg:
            if not hasattr(self,methodName):
                raise AttributeError("method '%s' is missing !" % methodName)
            
            fn = getattr(self,methodName)
            fnId = wx.NewId()
            self.Bind(wx.EVT_MENU, fn, id=fnId)
            table.append((key1,key2,fnId))    
        
        if len(table)>0:
            self.SetAcceleratorTable(wx.AcceleratorTable(table))
    
    ## callbacks
    def on_exit(self, event):
        self.Close()
        self.Destroy()
    
    def on_shell(self,event):
        self._shellDialog.Show()

if __name__ == "__main__":
    app = wx.App()
    fr = BaseFrame(None)

    # matplotlib scripting
    import numpy as np
    fig = fr.get_figure()
    axes = fig.add_subplot(111)
    t = np.arange(0,10,0.1)
    axes.plot(t,np.sin(t)/(1+t**2))
    # end
    fr.Show()
    app.MainLoop()       


