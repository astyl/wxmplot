
from abcmodel import AbcModel

class mFigure(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        # specific to the artist matplotlib.Figure
        "dpi": (int,"int",80,"figure dpi"),
        "facecolor": (str,"color","white","figure background color"),
        
        # children
        "maxes": (list,"model",[],"axes list"),
        
        # specific to wxmplot        
        "rows": (int,"int",1,"nb of rows"),
        "columns": (int,"int",1,"nb of columns"),
        
#         "margin_left": (int,"int",30,"margin left"),
#         "margin_top": (int,"int",30,"margin top"),
#         "margin_right": (int,"int",30,"margin right"),
#         "margin_bottom": (int,"int",30,"margin bottom"),
#         "margin_wspace": (int,"int",10,"margin wspace"),
#         "margin_hspace": (int,"int",10,"margin hspace"),

    })
    
    