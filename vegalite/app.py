from sklearn import datasets
import pandas as pd
from vega import VegaLite



wine = pd.DataFrame(datasets.load_wine().data)
wine.columns = datasets.load_wine().feature_names
print(wine)
# print(datasets)

VegaLite({
    "mark": "point",
    "encoding": {
        "y": {"type": "qantitative", "field": "alcohol"},
        "x": {"type": "qantitative", "field": "color_intensity"},
        "tooltip":[
            {"type": "nominal", "field": "ash"},
            {"type": "qantitative", "field": "alcohol"},
            {"type": "qantitative", "field": "color_intensity"}
        ]


    }

}, wine)

