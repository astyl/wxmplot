
import wx

# Plot Panel
from basepanel import BasePanel
def mplotPanel(parent):
    return BasePanel(parent)

# Plot Frame
from baseframe import BaseFrame
def mplotFrame():
    return BaseFrame(None)

# Plot App
def mplotApp():
    app = wx.App()
    frame = mplotFrame()
    app.SetTopWindow(frame)
    frame.Show()
    return app,frame.get_figure()

if __name__ == "__main__":
    app,figure = mplotApp()
    # matplotlib script
    import numpy as np
    figure.suptitle("wxmplot")
    axes = figure.add_subplot(1,1,1)
    t = np.arange(0,10,0.1)
    axes.plot(t,np.sin(t))
    # end 
    app.MainLoop()
