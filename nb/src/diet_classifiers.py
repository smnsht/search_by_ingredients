import sys
import os
from argparse import ArgumentParser
from typing import List
from time import time
import pandas as pd
##########################################################################################
import joblib
import re

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
#     # TODO: Implement
#     return False


# def is_ingredient_vegan(ingredient: str) -> bool:
#     # TODO: Implement
#     return False


def is_keto(ingredients: List[str]) -> bool:
    predicted = rf_keto_clf.predict(ingredients)
    return all(predicted)
    #return all(map(is_ingredient_keto, ingredients))


def is_vegan(ingredients: List[str]) -> bool:
    predicted = rf_vegan_clf.predict(ingredients)
    return all(predicted)
    #return all(map(is_ingredient_vegan, ingredients))


def main(args):
    def wrap_is_keto(ingr_str: str) -> bool:
        ingr_arr = re.findall(r"'(.*?)'", ingr_str)
        return is_keto(ingr_arr)
    
    def wrap_is_vegan(ingr_str: str) -> bool:
        ingr_arr = re.findall(r"'(.*?)'", ingr_str)
        return is_vegan(ingr_arr)
    

    ground_truth = pd.read_csv(args.ground_truth, index_col=None)
    try:
        start_time = time()
        # !!!
        # The data in 'ingredients' looks like serialized list, but it missing separating commas.
        # Example: 
        # ['2 cups all-purpose flour' '1/4 cup white sugar'
        #    '1/2 teaspoon vanilla extract' '1 cup margarine' '2 cups chopped pecans'
        #    "1/3 cup confectioners' sugar for decoration"]
        # IT NOT PASSED TO is_keto & is_vegan AS LIST, BUT AS A STRING
        # I'm fixing it my way - using helpers wrap_
        ground_truth['keto_pred'] = ground_truth['ingredients'].apply(wrap_is_keto)
        ground_truth['vegan_pred'] = ground_truth['ingredients'].apply(wrap_is_vegan)

        end_time = time()
    except Exception as e:
        print(f"Error: {e}")
        return -1

    print("===Keto===")
    print(classification_report(
        ground_truth['keto'], ground_truth['keto_pred']))
    print("===Vegan===")
    print(classification_report(
        ground_truth['vegan'], ground_truth['vegan_pred']))
    print(f"== Time taken: {end_time - start_time} seconds ==")
    return 0


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--ground_truth", type=str, default="/usr/src/data/ground_truth_sample.csv")
                        #default="nb/data/ground_truth_sample.csv")
                        
    sys.exit(main(parser.parse_args()))
