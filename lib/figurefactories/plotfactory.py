

def factor_plot(axes,mplot):
    # extract 
    X = mplot.get_X()
    Y = mplot.get_Y()
    color = mplot.get_color()
    linestyle = mplot.get_linestyle()
    
    
    # rearrange 
    plotArgs = {
        "color": color,
        "linestyle":  linestyle,
    }
    
    # configure
    axes.plot(X,Y,**plotArgs)