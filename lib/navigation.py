# -*-coding:Utf-8 -*
from matplotlib.backend_bases import NavigationToolbar2,cursors

import wx

class Navigation(NavigationToolbar2):
    cursord = {
        cursors.MOVE : wx.CURSOR_HAND,
        cursors.HAND : wx.CURSOR_HAND,
        cursors.POINTER : wx.CURSOR_ARROW,
        cursors.SELECT_REGION : wx.CURSOR_CROSS,
    }
    nav_mode = None
    
    def __init__(self,canvas,nav_mode,nav_messenger):
        NavigationToolbar2.__init__(self, canvas)
        self._nav_messenger = nav_messenger
        if nav_mode == "pan":
            self.pan()
        elif nav_mode == "zoom":
            self.zoom()
            
    def zoom(self):
        """ zoom/unzoom"""
        self._toggleMode("zoom")
        NavigationToolbar2.zoom(self)

    def pan(self, *args):
        """ pan/unpan"""
        self._toggleMode("pan")
        NavigationToolbar2.pan(self)

    def set_message(self, s):
        self._nav_messenger(s)

    def set_cursor(self, cursor):
        cursor =wx.StockCursor(self.cursord[cursor])
        self.canvas.SetCursor( cursor )

    def press(self, event):
        if self.nav_mode == 'zoom':
            self.wxoverlay = wx.Overlay()

    def release(self, event):
        if self.nav_mode == 'zoom':
            # When the mouse is released we reset the overlay and it
            # restores the former content to the window.
            self.wxoverlay.Reset()
            del self.wxoverlay

    def draw_rubberband(self, event, x0, y0, x1, y1):
        # Use an Overlay to draw a rubberband-like bounding box.

        dc = wx.ClientDC(self.canvas)
        odc = wx.DCOverlay(self.wxoverlay, dc)
        odc.Clear()

        # Mac's DC is already the same as a GCDC, and it causes
        # problems with the overlay if we try to use an actual
        # wx.GCDC so don't try it.
        if 'wxMac' not in wx.PlatformInfo:
            dc = wx.GCDC(dc)

        height = self.canvas.figure.bbox.height
        y1 = height - y1
        y0 = height - y0

        if y1<y0: y0, y1 = y1, y0
        if x1<y0: x0, x1 = x1, x0

        w = x1 - x0
        h = y1 - y0
        rect = wx.Rect(x0, y0, w, h)

        rubberBandColor = '#C0C0FF' # or load from config?

        # Set a pen for the border
        color = wx.NamedColour(rubberBandColor)
        dc.SetPen(wx.Pen(color, 1))

        # use the same color, plus alpha for the brush
        r, g, b = color.Get()
        color.Set(r,g,b, 0x60)
        dc.SetBrush(wx.Brush(color))
        dc.DrawRectangleRect(rect)
    
    def _init_toolbar(self):
        pass

    def _toggleMode(self,state):
        if self.nav_mode == state:
            self.nav_mode = None
        else:
            self.nav_mode = state

