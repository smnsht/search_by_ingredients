import json
from argparse import ArgumentParser
from typing import List
from time import time
import pandas as pd
##########################################################################################
import joblib

# Load the serialized models on Docker
#rf_vegan_clf = joblib.load('/app/data/grid_rf_vegan.pkl')
#rf_keto_clf = joblib.load('/app/data/grid_rf_keto.pkl')

# Load the serialized models on Windows
base_dir = 'C:/Users/SimonShtock/source/search_by_ingredients/web/src'
rf_vegan_clf = joblib.load(base_dir + '/grid_rf_vegan.pkl')
rf_keto_clf = joblib.load(base_dir + '/grid_rf_keto.pkl')
###########################################################################################
try:
    from sklearn.metrics import classification_report
except ImportError:
    # sklearn is optional
    def classification_report(y, y_pred):
        print("sklearn is not installed, skipping classification report")


# def is_ingredient_keto(ingredient: str) -> bool:
#     pass    


# def is_ingredient_vegan(ingredient: str) -> bool:    
#     pass


def is_keto(ingredients: List[str]) -> bool:    
    predicted = rf_keto_clf.predict(ingredients)
    return all(predicted)


def is_vegan(ingredients: List[str]) -> bool:
    predicted = rf_vegan_clf.predict(ingredients)
    return all(predicted)
