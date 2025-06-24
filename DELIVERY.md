# General Idea

My idea is to build 2 classifiers using classifiers, available in scikit-learn library.
I will evaluate several models and 2 vectorization techniques to find best solution.

For training I am using ingredients dataset from kaggle: (forgot it's url).
The dataset is downloaded and saved as food1.csv. 

The dataset does not indicates if the dataset is vegan or not, but we can infer this by analysing cholesterl - 
anymal food always have cholesterol in it, while non-anymal food have zero cholesterol.
One exception is eggs white, I am fixing this for ingredients containging "EGG,WHITE" (see code in diet_dataset.py).

The Column 'Data.Carbohydrate' from the ingredients dataset holds amount of hydrocarbs per 100g, exactly what we need
to determin if the ingredient is keto or not.

After evaluation best trained models are serialized into *.pkl fils: 
- **grid_rf_keto.pkl** (keto classifier)
- **grid_rf_vegan.pkl** (vegan classifier)

The classifier just load them and using to answer if the meal is keto and/or vegan.


## Attached Jupeter notebooks

I've attached 2 notebooks - **06_TfidfVectorizer.ipynb** and **07_CountVectorizer.ipynb**.
In each notebook several classifiers are evaluated agaings **groud_truth_sample.csv**.

Best model/vectorizer found in this reserch - TfidfVectorizer/RandomForestClassifier, it achtived 81% accuracy score for both classifiers.


### Running diet_classifiers.py locally

I have runned diet_classifiers.py locally, took a screenshot of results as an evidence - **nb/Screenshot_run1.png**.
In order to run: invoke command python nb/src/diet_classifiers.py from the root folder. 
The folder is importent, because my script must to find *.pkl files, and in order to do so it resolves related paths.
**!!!After running locally I've altered path, so the script will run correctly on Docker!!!**

### Running diet_classifiers.py in the Docker

I have runned diet_classifiers.py in the Docker, took a screenshot of results as an evidence - **nb/Screenshot_run2.png**.
Delivery version adapted for Docker, to invoke script: python diet_classifiers.py, as shown on the screenshot.


### Skipping implementation of **is_ingredient_keto** and **is_ingredient_vegan**

My classifiers are already works with lists, so implementing classifier for single ingredient is not required.
I implemented **is_keto(list)** and **is_vegan(list)**, while commenting out mentioned 2 methods.