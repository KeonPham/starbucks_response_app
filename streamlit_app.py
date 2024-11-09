import streamlit as st
import pandas as pd
import joblib

st.title(':blue[Starbucks Customer Response Prediction]')
st.write("""-- This app predicts whether a customer will respond to a specific offer --

""")
st.write(':point_left: (click arrow sign to hide or unhide the form) :green[Please fill out the input fields below for prediction.] :sunglasses:')

# Collect user input features into a DataFrame
def user_input_features():
    # Create columns for input fields to be side by side
    col1, col2, col3 = st.columns(3)
    
    with col1:
        amount = st.number_input('Total Transaction Amount ($): ')
        time = st.number_input('Time (minutes): ')
        age = st.number_input('Age of Customer: ')
        income = st.number_input('Annual Income ($): ')
        difficulty = st.number_input('Offer Difficulty (0, 5, 7, 10, 20): ')
        duration = st.number_input('Offer Duration (days) - (3, 4, 5, 7, 10): ')
        
    with col2:
        offer_type_bogo = st.slider('Proportion of Offer Type - BOGO (0-1 scale): ', 0.0, 1.0, 0.0)
        offer_type_discount = st.slider('Proportion of Offer Type - Discount (0-1 scale): ', 0.0, 1.0, 0.0)
        offer_type_informational = st.slider('Proportion of Offer Type - Informational (0-1 scale): ', 0.0, 1.0, 0.0)
        web = st.number_input('Number of Interactions via Web: ')
        email = st.number_input('Number of Interactions via Email: ')
        mobile = st.number_input('Number of Interactions via Mobile: ')
        
    with col3:
        social = st.number_input('Number of Interactions via Social Media: ')
        membership_duration = st.number_input('Membership Duration (days): ')
        difficulty_income_interaction = st.number_input('Difficulty-Income Interaction: ')
        gender_F = st.selectbox('Gender (Female=1, else=0)', (0, 1))
        gender_M = st.selectbox('Gender (Male=1, else=0)', (0, 1))
        gender_O = st.selectbox('Gender (Other=1, else=0)', (0, 1))
        year_become_member = st.number_input('Year Became a Member: ', min_value=2015, max_value=2024, step=1)
        month_become_member = st.number_input('Month Became a Member (1-12): ', min_value=1, max_value=12, step=1)
        date_become_member = st.number_input('Date Became a Member (1-31): ', min_value=1, max_value=31, step=1)

    data = {
        'amount': amount, 'time': time, 'age': age, 'income': income, 'difficulty': difficulty, 'duration': duration,
        'offer_type_bogo': offer_type_bogo, 'offer_type_discount': offer_type_discount,
        'offer_type_informational': offer_type_informational, 'web': web, 'email': email, 'mobile': mobile,
        'social': social, 'membership_duration': membership_duration, 'difficulty_income_interaction': difficulty_income_interaction,
        'gender_F': gender_F, 'gender_M': gender_M, 'gender_O': gender_O, 'year_become_member': year_become_member,
        'month_become_member': month_become_member, 'date_become_member': date_become_member
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.write(input_df)

def predict(data):
    clf = joblib.load("model_file.p")
    return clf.predict(data)

# Apply model to make predictions
if st.button("Click here to Predict Customer Response"):
    result = predict(input_df)

    if result[0] == 0:
        st.subheader('The Customer :red[will not respond] to the offer. :sunglasses:')
    elif result[0] == 1:
        st.subheader('The Customer :red[will partially respond] to the offer. :sunglasses:')
    else:
        st.subheader('The Customer :green[will respond] to the offer! :smiley:')
