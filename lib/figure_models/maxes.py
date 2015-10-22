
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
        "title": (unicode,"unicode",[],"axes title"),
        "axis_bgcolor": (unicode,"color",[],"axes background color"),
        "xlabel": (unicode,"unicode","","axes xlabel"),
        "ylabel": (unicode,"unicode","","axes ylabel"),
        "xlim": (list,"list",[None,None],"axes xlim"),
        "ylim": (list,"list",[None,None],"axes ylim"),
        
        # children
        "mplot": (list,"model",[],"mplot list"),
        
    })