# 🧪 Notebooks: NLP Exploration for the Hiring Challenge

This folder contains my **exploratory notebooks** for the hiring challenge.  
The original task asked for a full production pipeline (model saving, Flask integration, Docker, etc.), but here I focused purely on the **ML/NLP side** — experimenting, comparing, and understanding different text‑representation methods.

## 📓 What’s inside

- **TF‑IDF notebook**  
  A baseline experiment using scikit‑learn’s TF‑IDF vectorizer + several classic classifiers.  
  Good for understanding how far simple bag‑of‑words features can go.

- **Word2Vec notebook**  
  A small‑corpus experiment using gensim’s Word2Vec (skip‑gram).  
  Includes tokenization, embedding training, document vectorization, and classifier evaluation.

Both notebooks explore the same vegan/keto classification problem, but with different feature representations.

## 🎯 Goal of this folder

The aim here is **not** to squeeze out the best possible accuracy.  
Instead, this is a space for:

- playing with NLP libraries  
- comparing embedding strategies  
- visualizing and evaluating classifiers  
- understanding how small datasets behave with different text features

Think of it as a sandbox rather than a polished solution.

## 🧠 What you’ll find inside the notebooks

- simple preprocessing + tokenization  
- TF‑IDF vs Word2Vec document embeddings  
- experiments with multiple classifiers (LogReg, SVM, KNN, trees, etc.)  
- per‑class evaluation (vegan vs keto)  
- notes and observations along the way

## 📦 What’s *not* included here

The production‑oriented parts of the challenge —  
model serialization, Flask integration, Docker setup —  
are intentionally **not** part of this folder.
