## **What is it?**
Poker hand web app is an end-to-end project which uses machine learning and deep learning models
to predict the category of a poker hand based on the inputs given. It uses various models (summarized below) for the predictions. 
Just follow these 3 steps.

***STEPS:***
- Enter suits and ranks of all of your 5 cards.
- Choose a model to predict (can be used for comparative study).
- Click on predict button and see the results.

**Machine Learning Models:**
- *Random Forest Classifier* - A classifier that generates multiple decision trees and gets results on the basis of voting. 

    (Accuracy = 64.17%)
- *Adaboost Classifier* - A boosting classifier with a base estimator of random forest. 
    
    (Accuracy =  64.44%)                            
- *Voting Classifier* - This classifier uses many base classifiers and then generates results based on voting.
 
    
   (Accuracy =  63.52%)
- *Stacking Classifier* - A classifier that stacks many other base classifiers. 

    (Accuracy =  66.93%) 

**Deep Learning Models:**
- Deep Feed Forward Neural Network - A deep neural network that uses at least 4 hidden layers. 

  (Accuracy =  99.62%)
- Multi Layer Perceptron - Another form of neural network provided by sklearn. 

  (Accuracy =  97.61%)

**Manual Coded Method:**
- A manual hand coded program that gives the poker hand based on the input. 

  (Accuracy = 100%)

*Note:* The predictions rendered by the ML DL models are based on the data on which it was trained. However, in reality,
there are more combinations of the 10 categorical poker hands. Hence, even with 99% accuracy, the model can make mistake.
Therefore, it is advised to use manual coded method for validation.

#### Developer: Amaan Izhar [![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)](https://github.com/AI-14)