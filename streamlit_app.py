import streamlit as st
import pandas as pd
import joblib

# Set up page config for a better UI
st.set_page_config(page_title="Starbucks Customer Response Prediction", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { 
        background-color: #f5f5f5; 
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    .stNumberInput input, .stSelectbox select {
        border-radius: 5px;
        padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.title(':blue[Starbucks Customer Response Prediction]')
st.write("""---""")
st.markdown("""
    <div style='text-align: center;'>
        <p style="font-size: 16px;">This app predicts whether a customer will respond to a specific offer.</p>
        <p style="font-size: 14px; color: green;">Fill out the input fields below and click the button to get your prediction.</p>
    </div>
    """, unsafe_allow_html=True)

# Collect user input features into a DataFrame
st.write("""---""")
st.subheader("Please fill out the form below:")

# Create columns for input fields
col1, col2, col3 = st.columns(3)

with col1:
    amount = st.number_input('Total Transaction Amount ($): ', min_value=0.0, step=0.1)
    time = st.number_input('Time (minutes): ', min_value=0.0, step=0.1)
    age = st.number_input('Age of Customer: ', min_value=0, step=1)
    income = st.number_input('Annual Income ($): ', min_value=0.0, step=1000.0)
    difficulty = st.number_input('Offer Difficulty (0, 5, 7, 10, 20): ', min_value=0, step=1)
    duration = st.number_input('Offer Duration (days) - (3, 4, 5, 7, 10): ', min_value=0, step=1)

with col2:
    offer_type_bogo = st.slider('Proportion of Offer Type - BOGO (0-1 scale): ', 0.0, 1.0, 0.0, step=0.1)
    offer_type_discount = st.slider('Proportion of Offer Type - Discount (0-1 scale): ', 0.0, 1.0, 0.0, step=0.1)
    offer_type_informational = st.slider('Proportion of Offer Type - Informational (0-1 scale): ', 0.0, 1.0, 0.0, step=0.1)
    web = st.number_input('Number of Interactions via Web: ', min_value=0, step=1)
    email = st.number_input('Number of Interactions via Email: ', min_value=0, step=1)
    mobile = st.number_input('Number of Interactions via Mobile: ', min_value=0, step=1)

with col3:
    social = st.number_input('Number of Interactions via Social Media: ', min_value=0, step=1)
    membership_duration = st.number_input('Membership Duration (days): ', min_value=0, step=1)
    difficulty_income_interaction = st.number_input('Difficulty-Income Interaction: ', min_value=0.0, step=0.1)
    gender_F = st.selectbox('Gender (Female=1, else=0)', (0, 1))
    gender_M = st.selectbox('Gender (Male=1, else=0)', (0, 1))
    gender_O = st.selectbox('Gender (Other=1, else=0)', (0, 1))
    year_become_member = st.number_input('Year Became a Member: ', min_value=2015, max_value=2024, step=1)
    month_become_member = st.number_input('Month Became a Member (1-12): ', min_value=1, max_value=12, step=1)
    date_become_member = st.number_input('Date Became a Member (1-31): ', min_value=1, max_value=31, step=1)

# Compile input data into a DataFrame
data = {
    'amount': amount, 'time': time, 'age': age, 'income': income, 'difficulty': difficulty, 'duration': duration,
    'offer_type_bogo': offer_type_bogo, 'offer_type_discount': offer_type_discount,
    'offer_type_informational': offer_type_informational, 'web': web, 'email': email, 'mobile': mobile,
    'social': social, 'membership_duration': membership_duration, 'difficulty_income_interaction': difficulty_income_interaction,
    'gender_F': gender_F, 'gender_M': gender_M, 'gender_O': gender_O, 'year_become_member': year_become_member,
    'month_become_member': month_become_member, 'date_become_member': date_become_member
}
input_df = pd.DataFrame(data, index=[0])

# Display input data
st.write("""---""")
st.subheader("Your Input Data:")
st.dataframe(input_df)

# Prediction function
def predict(data):
    clf = joblib.load("model_file.p")
    return clf.predict(data)

# Apply model to make predictions
st.write("""---""")
if st.button("Click here to Predict Customer Response"):
    result = predict(input_df)
    if result[0] == 0:
        st.subheader('🔴 The Customer :red[will not respond] to the offer.')
    elif result[0] == 1:
        st.subheader('🟠 The Customer :orange[will partially respond] to the offer.')
    else:
        st.subheader('🟢 The Customer :green[will respond] to the offer! :smiley:')
