
from abcmodel import AbcModel


class mAxes(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        # y2 label ?
        # axes label size
        # grid color 
        # grid on/off
        # legend on / off
        # legend text size
        # legend frame
        # legend loc / (on/out plot ?)
        
        # specific to the artist matplotlib.axes.Axes
        "title": (str,"str","","axes title"),
        "axis_bgcolor": (str,"color","white","axes background color"),
        "xlabel": (str,"str","","axes xlabel"),
        "ylabel": (str,"str","","axes ylabel"),
        
        # children
        "mplot": (list,"model",[],"mplot list"),
        
        # specific to wxmplot
        "grid_row_min":(int,"int",0,"grid row min index for the axes"),
        "grid_row_max":(int,"int",1,"grid row max index for the axes"),
        "grid_col_min":(int,"int",0,"grid col min index for the axes"),
        "grid_col_max":(int,"int",1,"grid col max index for the axes"),        
        
    })