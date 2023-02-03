# Poker Hand
![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python)
![Machine Learning](https://img.shields.io/badge/-Machine%20Learning-566be8?style=flat)
![Deep Learning](https://img.shields.io/badge/-Deep%20Learning-366be8?style=flat)
![Sklearn](https://img.shields.io/badge/-Sklearn-1fb30e?style=flat)
![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-black?style=flat&logo=jupyter)
![Streamlit](https://img.shields.io/badge/-Streamlit-f0806c?style=flat)

# Table of contents
1. [Description](#description)
2. [Screenshots](#screenshots)
3. [Steps taken in this project](#project-steps)
4. [Installation and Usage](#installation-usage)

## Description <a name="description"></a>
Poker hand is a data web app designed for predicting what poker category a given set of cards belong to. It uses various machine learning and deep learning algorithms for prediction. Furthermore, to get 100% accuracy, a manually coded poker program was also provided for comparative study. The algorithms used are provided on the app's main page with their description and accuracies.

## Screenshots <a name="screenshots"></a>
<img src="res//Pic1.png" width="800" height="500"/>
<br>
<img src="res//Pic2.png" width="800" height="500"/>
<br>
<img src="res//Pic3.png" width="800" height="500"/>

## Steps taken in this project <a name="project-steps"></a>
- Data collection
- EDA & visualization
- Model selection & building it
- Evaluation of the models
- Saving the models
- Application program for real time usage

## Installation and Usage <a name="installation-usage"></a> 
- Requirements:
   - `python >= 3.6`
- `git clone https://github.com/AI-14/poker-hand.git` - clones the repository
- `cd poker-hand`
- `py -m venv yourVenvName` - creates a virtual environment
- `yourVenvName\Scripts\activate.bat` - activates the virtual environment
- `pip install -r requirements.txt` - installs all modules
- `streamlit run src\main.py` - runs the app
> Note: The model files .pkl and .h5 were removed due to their large size. Hence, to save them again from the jupyter notebook, run the algorithms in the notebook and then save them under **src\models***.

