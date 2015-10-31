
from abcmodel import AbcModel
import numpy as np

class mPlot(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        "X": (np.ndarray,"model",np.ndarray([]),"var X"),
        "Y": (np.ndarray,"model",np.ndarray([]),"var Y"),
        "color": (str,"color","blue","artist color"),
        "linestyle":  (str,"str","-","linestyle"),
        # and other ...
    })        
        
        
        
    