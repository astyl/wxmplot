
from abcmodel import AbcModel
import numpy as np

class mPlot(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        "X": (np.ndarray,"model",np.ndarray(),"var X"),
        "Y": (np.ndarray,"model",np.ndarray(),"var Y"),
        "color": (unicode,"color","blue","artist color"),
        "linestyle":  (unicode,"unicode","-","linestyle"),
        # and other ...
    })        
        
        
        
    