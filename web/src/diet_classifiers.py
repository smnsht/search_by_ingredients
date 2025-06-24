import json
from argparse import ArgumentParser
from typing import List
from time import time
import pandas as pd
##########################################################################################
import joblib
import os

# Load the serialized models
current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)

rf_vegan_clf = joblib.load(os.path.join(current_dir_path, 'vegan_clf.pkl'))
rf_keto_clf = joblib.load(os.path.join(current_dir_path, 'keto_clf.pkl'))
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
