
import wx
from basepanel import BasePanel

class BaseFrame(wx.Frame):
    """ 
    BaseFrame is a wx.Frame meant to be the top window application.
    
    It is delivered with :
    - basePanels management : 
        It can hold several panels if necessary (tabs/floating windows)
        Each base panel is embedded with a matplotlib.figure with possible 
        interactions..
        Arstists can be drawn on the figure directly (or indirectly) via 
        the figure (or via a building process from a figure model)
        
        
    - basic GUIs to configure the figureModel: 
        The figureModel building can generate complex matplotlib figure
        with several axes, different artists plot, legends, annotations, ...
        
        ///
        Fancy GUI for specific models are to be specified elsewhere...
        ///
        
    - Menubar management :
        Easy configuration with a dictionnary (automatic binding, etc..)
    
    - shellPanel 
    """
    basePanelIds = [-1] # baseFrame has at least one basePanel
    
    def __init__(self,parent,**kwargs):
        """ Constructor
        wx.Frame arguments
        """
        kwargs["title"] = kwargs.get("title","wxmplot")
        kwargs["size"] = kwargs.get("size",(800,600))
        wx.Frame.__init__(self, parent, **kwargs)
        
        self.basePanels = { bpId : BasePanel(self,id=bpId) \
                                for bpId in self.basePanelIds}
    
    def get_canvas(self,panelId = None):
        """ return the matplotlib canvas of the panel """
        if panelId is None:
            panelId = self.basePanelIds[0]
        return self.basePanels[panelId].get_canvas()
    
    def get_figure(self,panelId = None):
        """ return the matplotlib canvas of the figure """
        if panelId is None:
            panelId = self.basePanelIds[0]
        return self.basePanels[panelId].get_figure()

    def get_figure_model(self,panelId = None):
        if panelId is None:
            panelId = self.basePanelIds[0]
        return self.basePanels[panelId].figure_model

    def build(self,panelId = None):
        if panelId is None:
            panelIds = self.basePanelIds
        else:
            panelIds = [panelId]
            
        for panelId in panelIds:
            self.basePanels[panelId].build()
            self.onBuild(panelId)
        
    def onBuild(self,panelId):
        pass
#         shellPanel.refreshLocals(figure = panel.get_figure())
    
    def draw(self, panelId = None):
        if panelId is None:
            panelId = self.basePanelIds[0]
        return self.basePanels[panelId].draw()

    ## callbacks        
    def on_close(self, event):
        self.Destroy()

    def on_exit(self, event):
        self.Close()
        

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


