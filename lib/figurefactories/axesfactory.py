from plotfactory import factor_plot

def factor_axes(figure,gridspec,maxes):
    # extract
    title = maxes.get_title()
    axis_bgcolor = maxes.get_axis_bgcolor()
    xlabel = maxes.get_xlabel()
    ylabel = maxes.get_ylabel()
    imin = maxes.get_grid_row_min()
    imax = maxes.get_grid_row_max()
    jmin = maxes.get_grid_col_min()
    jmax = maxes.get_grid_col_max()
    
    # configure
    sub = gridspec[imin:imax,jmin:jmax]
    axes = figure.add_subplot(sub)
    
    axes.set_title(title)
    axes.set_axis_bgcolor(axis_bgcolor)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    
    for mplot in maxes.get_mplot():
        # do several plot onto the axes
        factor_plot(axes,mplot)   
                    
    return axes

