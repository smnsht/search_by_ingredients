import pandas as pd

def load_foods(path):
    food_df = pd.read_csv(path, usecols=['Description', 'Data.Carbohydrate', 'Data.Cholesterol'])
    
    new_rows = pd.DataFrame([
        {"Description": 'SUGARS,WHITE', "Data.Carbohydrate": 100, 'Data.Cholesterol': 0},
        {"Description": 'BAKING SODA', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},
        {"Description": 'WATER', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},    
        {"Description": 'SALT,PEPPER', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},
        {"Description": 'PEPPER,BLACK', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},
        {"Description": 'ICE,CUBES', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},
        {"Description": 'GARBANZO,BEANS', "Data.Carbohydrate": 60, 'Data.Cholesterol': 0},      
        {"Description": 'OIL,CORN', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},      
        {"Description": 'TOMATOES,ROMA', "Data.Carbohydrate": 2.4, 'Data.Cholesterol': 0},      
        {"Description": 'TOMATOES,PLUM', "Data.Carbohydrate": 2.4, 'Data.Cholesterol': 0},
        {"Description": 'OLIVES,GREEN', "Data.Carbohydrate": 6, 'Data.Cholesterol': 0},
        {"Description": 'OLIVES,BLACK', "Data.Carbohydrate": 6, 'Data.Cholesterol': 0},
        {"Description": 'OLIVES,OIL', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},
        {"Description": 'OLIVES,OIL', "Data.Carbohydrate": 0, 'Data.Cholesterol': 0},
        {"Description": 'SAUCE,SOY', "Data.Carbohydrate": 4.9, 'Data.Cholesterol': 0},
        {"Description": 'APPLES', "Data.Carbohydrate": 13.8, 'Data.Cholesterol': 0},        
        {"Description": 'EGG', "Data.Carbohydrate": 0.0, 'Data.Cholesterol': 100},
        {"Description": 'EGGS', "Data.Carbohydrate": 0.0, 'Data.Cholesterol': 100},
        {"Description": 'BUTTER', "Data.Carbohydrate": 0.0, 'Data.Cholesterol': 100},   
        {"Description": 'MILK,CASHEW', "Data.Carbohydrate": 2.0, 'Data.Cholesterol': 0},   
        {"Description": 'MILK,COCONUT', "Data.Carbohydrate": 13.0, 'Data.Cholesterol': 0},         
    ])

    food_df = pd.concat([food_df, new_rows], ignore_index=True) 
    food_df['keto'] = food_df['Data.Carbohydrate'].apply(lambda gr: gr < 10)
    food_df['vegan'] = food_df['Data.Cholesterol'].apply(lambda ml: ml == 0)

    food_df.loc[food_df["Description"].str.contains("EGG,WHITE"), "vegan"] = False
    
    return food_df