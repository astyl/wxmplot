#!/usr/bin/env python

import wx
import matplotlib
from matplotlib.lines import Line2D
from navigation import Navigation
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure
from logger import LogClass


class BasePanel(wx.Panel,LogClass):
    """
    wx.Panel component.

    provides:
         Basic support Zooming / Unzooming
         support for Printing
         popup menu
         bindings for keyboard short-cuts
    """
    """ 'figure_model' holds the data to build a
    complex matplotlib figure with several 
    axes and artists plot    
    """
    figure_model = None
    """ 'shortcutCfg' configure the short-cuts to bind on the panel 
        Example :
            shortcutCfg = [ (wx.ACCEL_ALT, ord('X'), "onAltX"), ]
            with "onAltX" the method  name
    """
    shortcutCfg = []
    """ navigation """
    nav_mode = "zoom" # or "pan" or None
    nav_messenger = LogClass.log.debug
    
    def __init__(self,*args,**kwargs):
        """ Constructor
        wx.Panel arguments
        """ 
        wx.Panel.__init__(self,*args,**kwargs)
        
        # figure matplotlib
        self.__figure = Figure()
        # canvas matplotlib and panel
        self.__canvas = FigureCanvasWxAgg(self, -1, self.__figure)
        # navigation (zoom/unzoom)
        self.__navigation = Navigation(self.__canvas,self.nav_mode,self.nav_messenger)
        # short_cuts to bind
        self._set_shortcuts()
        # panel fit
        self._layout()
    
    def draw(self):
        self.__canvas.draw()

    def get_figure(self):
        return self.__figure
    
    def get_canvas(self):
        return self.__canvas
    
    def _set_shortcuts(self):
        table = []
        for key1,key2,methodName in self.shortcutCfg:
            if not hasattr(self,methodName):
                raise AttributeError("method %s missing !" % methodName)
            
            fn = getattr(self,methodName)
            fnId = wx.NewId()
            self.Bind(wx.EVT_MENU, fn, id=fnId)
            table.append((key1,key2,fnId))    
        
        if len(table)>0:
            self.SetAcceleratorTable(wx.AcceleratorTable(table))
            
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

    def build_figure(self,*args,**kwargs):
        self.__figure.clear()
        if self.__slide is None:
            return 
        ### TO BE REFACTORED WITH A GREAT FIGURE FACTORY 
        # Slide
        title = self.__slide.get_title()
        projections = self.__slide.get_projections()
        
        self.__figure.suptitle(title)
        self.__figure.abcModel = self.__slide
        
        # Projection
        for i,projection in enumerate(projections):
            collections = projection.get_collections()
            xlabel = projection.get_xlabel()
            ylabel = projection.get_ylabel()
            xlim = projection.get_xmin(),projection.get_xmax()
            ylim = projection.get_ymin(),projection.get_ymax()
            
            axes = self.__figure.add_subplot(len(projections),1,i+1)
            axes.set_xlabel(xlabel)
            axes.set_ylabel(ylabel)
            axes.set_xlim(xlim)
            axes.set_ylim(ylim)

            axes.abcModel = projection
            
            for collection in collections:
                # Collection
                X = collection.get_X().get_data()
                Y = collection.get_Y().get_data()
                pL = ["color","linestyle"]
                kw = { k: collection.getAttr(k) \
                                            for k in pL} 
                
                line = Line2D(X,Y,**kw)
                axes.add_line(line)
                
                line.abcModel = collection
                


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