
from abcmodel import AbcModel

class mFigure(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        # specific to the artist matplotlib.Figure
        "title": (unicode,"unicode",[],"figure title"),
        "face_color": (unicode,"color",[],"figure background color"),
        
        # children
        "maxes": (list,"model",[],"axes list"),
        
        # specific to wxmplot        
        "margin_left": (float,"float",30.0,"margin left"),
        "margin_top": (float,"float",30.0,"margin top"),
        "margin_right": (float,"float",30.0,"margin right"),
        "margin_bottom": (float,"float",30.0,"margin bottom"),
        "margin_wspace": (float,"float",10.0,"margin wspace"),
        "margin_hspace": (float,"float",10.0,"margin hspace"),

        "grid_row_min":(list,"list",[],"grid row min indexes for the axes list"),
        "grid_row_max":(list,"list",[],"grid row max indexes for the axes list"),
        "grid_col_min":(list,"list",[],"grid col min indexes for the axes list"),
        "grid_col_max":(list,"list",[],"grid col max indexes for the axes list"),

    })
    
    