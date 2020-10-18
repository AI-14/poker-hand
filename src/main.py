#Importing libraries.
import streamlit as st
import numpy as np
import pickle
from keras.models import load_model
from models.hand_coded_poker import get_poker_hand
import codecs

poker_hand_descr = {
                    0: 'Nothing in hand => Not a recognized poker hand.',
                    1: 'One pair => One pair of equal ranks within five cards.',
                    2: 'Two pairs => Two pairs of equal ranks within five cards.',
                    3: 'Three of a kind => Three equal ranks within five cards.',
                    4: 'Straight => Five cards, sequentially ranked with no gaps.',
                    5: 'Flush => Five cards with the same suit.',
                    6: 'Full house => Pair + different rank three of a kind.',
                    7: 'Four of a kind => Four equal ranks within five cards.',
                    8: 'Straight flush => Straight + flush.',
                    9: 'Royal flush => {Ace, King, Queen, Jack, Ten} + flush.'
                   }

def home():
    '''
    Description:
        Method for initializing the main page's content.

    Parameters:
        None
    
    Returns:
        None
    '''

    title = codecs.open('src//res_md//title.md', 'r', 'utf-8')
    info = codecs.open('src//res_md//info.md', 'r', 'utf-8')

    st.markdown(title.read(), unsafe_allow_html=True)
    st.write('\n\n')
    st.markdown(info.read())

def predictions():
    '''
    Description:
        Method to make predictions and display the results according to the model selected by the user.
        
    Parameters:
        None
    
    Returns:
        None
    '''

    input_data = make_get_input_fields()
    encoded_data_array = np.array(input_data).reshape(1, -1)
    st.write('Encoded data array:')
    st.write(encoded_data_array)
    model = get_classifier_model()
    with st.beta_expander('POKER HANDS CATEGORY:'):
        st.write(poker_hand_descr)

    if st.button('Predict my hand'):
        if model[0] in ['Random Forest Classifier', 'Adaboost Classifier', 'Voting Classifier', 'Stacking Classifier', 'Multi Layer Perceptron']:
            poker_hand_prediction = model[1].predict(encoded_data_array)
            st.success(f'Your Hand: {poker_hand_descr[poker_hand_prediction[0]]}')
        elif model[0] == 'Deep Feed Forward Neural Network':
            poker_hand_prediction = model[1].predict(encoded_data_array)
            st.success(f'Your Hand: {poker_hand_descr[poker_hand_prediction.argmax()]}')
        else:
            st.success(f'Your Hand: {poker_hand_descr[get_poker_hand(input_data)]}')

def make_get_input_fields():
    '''
    Description:
        Method to make input fields and returning the options chosen by the user.

    Parameters:
        None
    
    Returns:
        A list => containing all the suites and ranks of all the five cards.
    '''

    suite_dict = {'Hearts': 1,
                  'Spades': 2,
                  'Diamonds': 3,
                  'Clubs': 4}
    rank_dict = {'Ace': 1,
                 'Jack': 11,
                 'Queen': 12,
                 'King': 13
                 }

    col1, col2, col3, col4, col5 = st.beta_columns(5) #Splitting the layout into 5 columns.

    with col1:
        s1 = st.selectbox('Suite Of Card 1', ['Hearts', 'Clubs', 'Diamonds', 'Spades'])
        s1 = suite_dict[s1]
        c1 = st.selectbox('Rank Of Card 1', ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'])
        if c1 in ['Ace', 'Jack', 'Queen', 'King']:
            c1 = rank_dict[c1] #Getting the numerical value.

    with col2:
        s2 = st.selectbox('Suite Of Card 2', ['Hearts', 'Clubs', 'Diamonds', 'Spades'])
        s2 = suite_dict[s2]
        c2 = st.selectbox('Rank Of Card 2', ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'])
        if c2 in ['Ace', 'Jack', 'Queen', 'King']:
            c2 = rank_dict[c2] #Getting the numerical value.

    with col3:
        s3 = st.selectbox('Suite Of Card 3', ['Hearts', 'Clubs', 'Diamonds', 'Spades'])
        s3 = suite_dict[s3]
        c3 = st.selectbox('Rank Of Card 3', ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'])
        if c3 in ['Ace', 'Jack', 'Queen', 'King']:
            c3 = rank_dict[c3] #Getting the numerical value.

    with col4:
        s4 = st.selectbox('Suite Of Card 4', ['Hearts', 'Clubs', 'Diamonds', 'Spades'])
        s4 = suite_dict[s4]
        c4 = st.selectbox('Rank Of Card 4', ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'])
        if c4 in ['Ace', 'Jack', 'Queen', 'King']:
            c4 = rank_dict[c4] #Getting the numerical value.

    with col5:
        s5 = st.selectbox('Suite Of Card 5', ['Hearts', 'Clubs', 'Diamonds', 'Spades'])
        s5 = suite_dict[s5]
        c5 = st.selectbox('Rank Of Card 5', ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'])
        if c5 in ['Ace', 'Jack', 'Queen', 'King']:
            c5 = rank_dict[c5] #Getting the numerical value.

    hand_data = [s1, c1, s2, c2, s3, c3, s4, c4, s5, c5] #Combining in the format that our model expects.
    return hand_data

def get_classifier_model():
    '''
    Description:
        Method that loads a machine learning or deep learning model and returns it.
        
    Parameters:
        None
    
    Returns:
        A list => containing name of the classifier and the model itself. The model can be
                  a pickle or a keras loaded model. Only in the 'Manual Model' selection, it returns
                  a None object in place of the model.
    '''

    model_name = st.selectbox('Choose a model',
                              ['Random Forest Classifier', 'Adaboost Classifier', 'Voting Classifier', 'Stacking Classifier',
                               'Deep Feed Forward Neural Network', 'Multi Layer Perceptron', 'Manual Model'])

    if model_name == 'Random Forest Classifier':
        return ['Random Forest Classifier', pickle.load(open('src//models//random_forest.pkl', 'rb'))]
    elif model_name == 'Adaboost Classifier':
        return ['Adaboost Classifier', pickle.load(open('src//models//adaboost_random_forest.pkl', 'rb'))]
    elif model_name == 'Voting Classifier':
        return ['Voting Classifier', pickle.load(open('src//models//voting_classifier.pkl', 'rb'))]
    elif model_name == 'Stacking Classifier':
        return ['Stacking Classifier', pickle.load(open('src//models//stacking_classifier.pkl', 'rb'))]
    elif model_name == 'Deep Feed Forward Neural Network':
        return ['Deep Feed Forward Neural Network', load_model('src//models//dl_v1.h5')]
    elif model_name == 'Multi Layer Perceptron':
        return ['Multi Layer Perceptron', pickle.load(open('src//models//dl_v2.pkl', 'rb'))]
    else:
        return ['Hand Coded Model', None]

def conclusions():
    '''
    Description:
        Displays conclusion/insights about the whole project.

    Parameters:
            None

    Returns:
        None
    '''

    conclusion = codecs.open('src//res_md//conclusion.md', 'r', 'utf-8')
    st.markdown(conclusion.read(), unsafe_allow_html=True)

    if st.button('Thank You'):
        st.balloons()

def main():
    '''
    Description:
        Main method. All the functionalities goes here.

    Parameters:
        None
    
    Returns:
        None
    '''
    
    st.sidebar.title('Navigate')
    navigation = st.sidebar.radio('', ['Home', 'Use Models', 'Conclusions/Insights'])
    if navigation == 'Home':
        home()
    if navigation == 'Use Models':
       predictions()
    if navigation == 'Conclusions/Insights':
        conclusions()


# Application starts here.
if __name__ == '__main__':
    main()