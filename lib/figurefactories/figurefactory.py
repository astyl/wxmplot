from matplotlib.gridspec import GridSpec
from axesfactory import factor_axes

def factor_figure(figure,mfigure):
    # clear
    figure.clear()
    
    if mfigure is None:
        return
    
    # extract 
    dpi = mfigure.get_dpi()
    facecolor = mfigure.get_facecolor()
    rows = mfigure.get_rows()
    columns = mfigure.get_columns()
    
    # configure
    figure.set_dpi(dpi)
    figure.set_facecolor(facecolor)
    
    gridspec = GridSpec(rows,columns)
    for maxes in mfigure.get_maxes():
        factor_axes(figure,gridspec,maxes)
    
    
    
