# Poker Hand
  ![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python)
  ![Machine Learning](https://img.shields.io/badge/-Machine%20Learning-566be8?style=flat)
  ![Deep Learning](https://img.shields.io/badge/-Deep%20Learning-366be8?style=flat)
  ![Sklearn](https://img.shields.io/badge/-Sklearn-1fb30e?style=flat)
  ![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-black?style=flat&logo=jupyter)
  ![Streamlit](https://img.shields.io/badge/-Streamlit-f0806c?style=flat)

## Description
   Poker hand is a data web app designed for predicting what poker category a given set of cards belong to. It uses various machine learning and deep learning algorithms for        prediction. Furthermore, to get 100% accuracy, a manually coded poker program was also provided for comparative study. The algorithms used are provided on the app's main page 
   with their description and accuracies.

## Screenshots Of The App
<details>
  <summary>Click to expand!</summary>
  <br/>

<img src="res//Pic1.png" width="800" height="500"/>
<br>
<img src="res//Pic2.png" width="800" height="500"/>
<br>
<img src="res//Pic3.png" width="800" height="500"/>
</details>

## Steps Taken In This Project
<details>
  <summary>Click to expand!</summary>
  <br/>

- Data Collection
- EDA & Visualization
- Model selection & building it.
- Evaluation of the models.
- Saving the models.
- Application program for real time usage.
</details>

## Installation And Usage
<details>
  <summary>Click to expand!</summary>
  <br/>

1. Installation
   - Download/clone this repository. Then open terminal (make sure you are in the project's directory).
   - Create a virtual environment using the command ````py -m venv yourVenvName```` and activate it using ````yourVenvName\Scripts\activate.bat````.
   - Then run the following command ````pip install -r requirements.txt````. With this, all the dependencies will be installed in your virtual environment. 
> **Note:** *If any dependency is missing or an error shows up, install it using ````pip install moduleName````*.

2. Usage
   - Open your project folder and go to the terminal and activate your virtual environment. Then type ````streamlit run src\main.py```` and the app will open in your web 
   browser. Now you can interact with it or play with the code and add your own features. Also you can play around with jupyter notebook if you wish. 
> **Note:** *The model files .pkl and .h5 were removed due to their large size. Hence, to save them again from the jupyter notebook, run the algorithms in the notebook and then 
             save them under **src//models***.
</details>
