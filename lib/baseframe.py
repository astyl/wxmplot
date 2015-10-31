
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
    
    def get_panel(self,panelId = None):
        """ return a base panel """
        if panelId is None:
            panelId = self.panelIds[0]
        return self.panels[panelId]
                    
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
        
    def build_figure(self, panelId = None):
        """ build a figure on the panel """
        if panelId is None:
            panelIds = [self.panelIds[0]]
        else:
            panelIds = self.panelIds
        for panelId in panelIds:
            self.panels[panelId].build_figure()

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

#     # matplotlib scripting
#     import numpy as np
#     fig = fr.get_figure()
#     axes = fig.add_subplot(111)
#     t = np.arange(0,10,0.1)
#     axes.plot(t,)
#     # end
    panel = fr.get_panel()
    import numpy as np
    from figuremodels.mfigure import mFigure
    from figuremodels.maxes import mAxes
    from figuremodels.mplot import mPlot
    mf = mFigure()
    ma = mAxes()
    mp1= mPlot()
    mp2= mPlot()
    
    X = np.arange(0,10,0.1)
    Y1= np.sin(X)/(1+X**2)
    Y2= np.cos(X)/(1+X**2)
    mp1.update(name="mp1",X=X,Y=Y1,color="red",linestyle="--")
    mp2.update(name="mp2",X=X,Y=Y2,color="blue")
    ma.update(name="ma",xlabel="t",ylabel="y1",mplot=[mp1,mp2])
    mf.update(name="mf",facecolor="grey",maxes=[ma])
    fr.get_panel().set_mfigure(mf)
    fr.Show()

    fr.build_figure()
    fr.draw()
    app.MainLoop()       


