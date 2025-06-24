# General Idea

My idea is to build two classifiers using available models from the **scikit-learn** library. I will evaluate several models and two vectorization techniques to find the best solution.

For training, I'm using an ingredients dataset from Kaggle (URL forgotten). The dataset has been downloaded and saved as **food1.csv**.

The dataset doesn't indicate whether an ingredient is vegan, but we can infer this by analyzing cholesterol levels. Animal products always contain cholesterol, while plant-based foods have zero cholesterol. One exception is egg whites, which I've addressed for ingredients containing "EGG,WHITE" (see code in **diet_dataset.py**).

The 'Data.Carbohydrate' column from the ingredients dataset holds the amount of carbohydrates per 100g, which is exactly what we need to determine if an ingredient is keto.

After evaluation, the best-trained models are serialized into **.pkl** files:

* **grid\_rf\_keto.pkl** (keto classifier)
* **grid\_rf\_vegan.pkl** (vegan classifier)

The classifier simply loads these files and uses them to determine if a meal is keto and/or vegan.

---

## Attached Jupyter Notebooks

I've attached two notebooks: **06\_TfidfVectorizer.ipynb** and **07\_CountVectorizer.ipynb**. In each notebook, several classifiers are evaluated against **ground\_truth\_sample.csv**.

The best model/vectorizer combination found in this research is **TfidfVectorizer** with **RandomForestClassifier**, achieving an 81% accuracy score for both classifiers.

---

### Running **diet\_classifiers.py** Locally

I've run **diet\_classifiers.py** locally and captured a screenshot of the results as evidence: **nb/Screenshot\_run1.png**. To run the script, execute `python nb/src/diet_classifiers.py --ground_truth nb/data/ground_truth_sample.csv` from the root folder. 

---

### Running **diet\_classifiers.py** in Docker

I've run **diet\_classifiers.py** in Docker and captured a screenshot of the results as evidence: **nb/Screenshot\_run2.png**. The delivery version is adapted for Docker; to invoke the script, use `python diet_classifiers.py`, as shown in the screenshot.

---

### Running **web** in Docker (broken)

I tackled several problems while tring to lauch web Docker: source files are not copied to the image, connection to OpenConnect failed, etc...
I tryed to to fix this - web/Docker is altered, but without success (OpenConnect connection failing), giving up on web Docker.
In order to run web app locally: manually alter paths to *.pkl files in web/src/diet_classifiers.py

---

### Skipping Implementation of `is_ingredient_keto` and `is_ingredient_vegan`

My classifiers already work with lists, so implementing classifiers for single ingredients is not required. I've implemented `is_keto(list)` and `is_vegan(list)` while commenting out the aforementioned two methods.