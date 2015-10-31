import wx
import matplotlib
from navigation import Navigation
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure
from logger import LogClass
from figurefactories.figurefactory import factor_figure

class BasePanel(wx.Panel,LogClass):
    """
    wx.Panel component.

    provides:
         matplotlib figure
         navigation (pan/zoom/print)
         bindings for keyboard short-cuts
    """
    # navigation
    nav_mode = "zoom" # or "pan" or None
    nav_messenger = LogClass.log.debug
    
    def __init__(self,*args,**kwargs):
        """ Constructor
        wx.Panel arguments
        """ 
        wx.Panel.__init__(self,*args,**kwargs)
        # figure matplotlib
        self.__figure = Figure()
        # canvas matplotlib and wxpanel
        self.__canvas = FigureCanvasWxAgg(self, -1, self.__figure)
        # navigation (zoom/unzoom)
        self.__navigation = Navigation(self.__canvas,self.nav_mode,self.nav_messenger)
        # figure model
        self.__mfigure = None
        # panel fit
        self._layout()
    
    def build_figure(self):
        factor_figure(self.__figure,self.__mfigure)

    def draw(self):
        self.__canvas.draw()

    def get_figure(self):
        return self.__figure
    
    def get_canvas(self):
        return self.__canvas
    
    def get_mfigure(self):
        return self.__mfigure
    
    def set_mfigure(self,mfigure):
        self.__mfigure = mfigure
    
    def print_figure(self, filename, dpi=None, facecolor='w', edgecolor='w',
                     orientation='portrait', format=None, **kwargs):
        self.__canvas.print_figure(filename, dpi=dpi, facecolor=facecolor, edgecolor=edgecolor,
                     orientation=orientation, format=format, **kwargs)

    def _layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.__canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(sizer)
        self.Fit()   
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    fr = wx.Frame(None)
    bp = BasePanel(fr)
    # matplotlib scripting
    import numpy as np
    fig = bp.get_figure()
    axes = fig.add_subplot(111)
    t = np.arange(0,10,0.1)
    axes.plot(t,np.sin(t)/(1+t**2))
    # end
    fr.Show()
    app.MainLoop()