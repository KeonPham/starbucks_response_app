# import streamlit as st
# import pandas as pd
# import joblib

# # Set up page config for a better UI
# st.set_page_config(page_title="Starbucks Customer Response Prediction", layout="wide")

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .main { 
#         background-color: #f5f5f5; 
#         padding: 20px;
#         border-radius: 10px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 5px;
#         padding: 10px 20px;
#         margin-top: 10px;
#     }
#     .stNumberInput input, .stSelectbox select {
#         border-radius: 5px;
#         padding: 5px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # App header
# st.title(':blue[Starbucks Customer Response Prediction]')
# st.write("""---""")
# st.markdown("""
#     <div style='text-align: center;'>
#         <p style="font-size: 16px;">This app predicts whether a customer will respond to a specific offer.</p>
#         <p style="font-size: 14px; color: green;">Fill out the input fields below and click the button to get your prediction.</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Collect user input features into a DataFrame
# st.write("""---""")
# st.subheader("Please fill out the form below:")

# # Create columns for input fields
# col1, col2, col3 = st.columns(3)

# with col1:
#     reward = st.number_input('Reward Offer ($): ', min_value=0.0, step=0.1)
#     time_received = st.number_input('Average Time Received Offer (hours): ', min_value=0.0, step=0.1)
#     age = st.number_input('Age of Customer: ', min_value=0, step=1)
#     income = st.number_input('Annual Income ($): ', min_value=0.0, step=1000.0)
#     difficulty = st.number_input('Total Offer Difficulty: ', min_value=0.0, step=0.1)
#     duration = st.number_input('Offer Duration (days): ', min_value=0, step=1)

# with col2:
#     membership_duration = st.number_input('Membership Duration (days): ', min_value=0, step=1)
#     web = st.number_input('Number of Interactions via Web: ', min_value=0, step=1)
#     email = st.number_input('Number of Interactions via Email: ', min_value=0, step=1)
#     mobile = st.number_input('Number of Interactions via Mobile: ', min_value=0, step=1)
#     social = st.number_input('Number of Interactions via Social Media: ', min_value=0, step=1)

# with col3:
#     offer_type_bogo = st.number_input('Number of Offer BOGO: ', min_value=0, step=1)
#     offer_type_discount = st.number_input('Number of Offer Discount: ', min_value=0, step=1)
#     offer_type_informational = st.number_input('Number Offer Informational: ', min_value=0, step=1)
#     gender_female = st.selectbox('Gender Female (binary): ', (0, 1))
#     gender_male = st.selectbox('Gender Male (binary): ', (0, 1))
#     gender_others = st.selectbox('Gender Others (binary): ', (0, 1))
#     year_become_member = st.number_input('Year Became a Member: ', min_value=2015, max_value=2024, step=1)
#     month_become_member = st.number_input('Month Became a Member (1-12): ', min_value=1, max_value=12, step=1)
#     date_become_member = st.number_input('Date Became a Member (1-31): ', min_value=1, max_value=31, step=1)

# # Automatically calculate difficulty-income interaction
# difficulty_income_interaction = difficulty * income

# # Compile input data into a DataFrame
# data = {
#     'reward': reward, 'time_received': time_received, 'age': age, 'income': income,
#     'difficulty': difficulty, 'duration': duration, 'membership_duration': membership_duration,
#     'web': web, 'email': email, 'mobile': mobile, 'social': social,
#     'offer_type_bogo': offer_type_bogo, 'offer_type_discount': offer_type_discount,
#     'offer_type_informational': offer_type_informational, 'difficulty_income_interaction': difficulty_income_interaction,
#     'gender_female': gender_female, 'gender_male': gender_male, 'gender_others': gender_others,
#     'year_become_member': year_become_member, 'month_become_member': month_become_member,
#     'date_become_member': date_become_member
# }
# input_df = pd.DataFrame(data, index=[0])

# # Display input data
# st.write("""---""")
# st.subheader("Your Input Data:")
# st.dataframe(input_df)

# # Prediction function
# def predict(data):
#     clf = joblib.load("model_file_best_xgb.p")
#     prediction = clf.predict(data)
#     probabilities = clf.predict_proba(data)
#     return prediction, probabilities

# # Apply model to make predictions
# st.write("""---""")
# if st.button("Click here to Predict Customer Response"):
#     result, probabilities = predict(input_df)
#     probability = probabilities[0][result[0]] * 100
#     if result[0] == 0:
#         st.subheader(f'🔴 The Customer :red[will not respond] to the offers. Probability: {probability:.2f}%')
#     elif result[0] == 1:
#         st.subheader(f'🟠 The Customer :orange[will partially respond] to the offers. Probability: {probability:.2f}%')
#     else:
#         st.subheader(f'🟢 The Customer :green[will respond] to the offers! Probability: {probability:.2f}% :smiley:')


import streamlit as st
import pandas as pd
import joblib
import io

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
        <p style="font-size: 16px;">This app predicts whether customers will respond to a specific offer.</p>
        <p style="font-size: 14px; color: green;">You can either fill out the form or upload an Excel file for batch predictions.</p>
    </div>
    """, unsafe_allow_html=True)

# Option to choose input method
st.write("""---""")
st.subheader("Choose Input Method:")
input_option = st.radio("How would you like to provide input?", ["Manual Input", "Upload Excel File"])

if input_option == "Manual Input":
    # Collect user input features into a DataFrame
    st.subheader("Fill out the form below:")

    # Create columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        reward = st.number_input('Reward Offer ($): ', min_value=0.0, step=0.1)
        time_received = st.number_input('Time Received (hours): ', min_value=0.0, step=0.1)
        age = st.number_input('Age of Customer: ', min_value=0, step=1)
        income = st.number_input('Annual Income ($): ', min_value=0.0, step=1000.0)
        difficulty = st.number_input('Offer Difficulty: ', min_value=0.0, step=0.1)
        duration = st.number_input('Offer Duration (days): ', min_value=0, step=1)

    with col2:
        membership_duration = st.number_input('Membership Duration (days): ', min_value=0, step=1)
        web = st.number_input('Number of Interactions via Web: ', min_value=0, step=1)
        email = st.number_input('Number of Interactions via Email: ', min_value=0, step=1)
        mobile = st.number_input('Number of Interactions via Mobile: ', min_value=0, step=1)
        social = st.number_input('Number of Interactions via Social Media: ', min_value=0, step=1)

    with col3:
        offer_type_bogo = st.number_input('Offer Type BOGO (binary): ', min_value=0, max_value=1, step=1)
        offer_type_discount = st.number_input('Offer Type Discount (binary): ', min_value=0, max_value=1, step=1)
        offer_type_informational = st.number_input('Offer Type Informational (binary): ', min_value=0, max_value=1, step=1)
        gender_female = st.selectbox('Gender Female (binary): ', (0, 1))
        gender_male = st.selectbox('Gender Male (binary): ', (0, 1))
        gender_others = st.selectbox('Gender Others (binary): ', (0, 1))
        year_become_member = st.number_input('Year Became a Member: ', min_value=2015, max_value=2024, step=1)
        month_become_member = st.number_input('Month Became a Member (1-12): ', min_value=1, max_value=12, step=1)
        date_become_member = st.number_input('Date Became a Member (1-31): ', min_value=1, max_value=31, step=1)

    # Automatically calculate difficulty-income interaction
    difficulty_income_interaction = difficulty * income

    # Compile input data into a DataFrame
    data = {
        'reward': reward, 'time_received': time_received, 'age': age, 'income': income, 
        'difficulty': difficulty, 'duration': duration, 'membership_duration': membership_duration, 
        'web': web, 'email': email, 'mobile': mobile, 'social': social, 
        'offer_type_bogo': offer_type_bogo, 'offer_type_discount': offer_type_discount, 
        'offer_type_informational': offer_type_informational, 'difficulty_income_interaction': difficulty_income_interaction,
        'gender_female': gender_female, 'gender_male': gender_male, 'gender_others': gender_others, 
        'year_become_member': year_become_member, 'month_become_member': month_become_member, 
        'date_become_member': date_become_member
    }
    input_df = pd.DataFrame(data, index=[0])

    # Display input data
    st.write("""---""")
    st.subheader("Your Input Data:")
    st.dataframe(input_df)

else:
    # Upload Excel file for batch predictions
    uploaded_file = st.file_uploader("Upload an Excel file:", type=["xlsx"])
    if uploaded_file:
        input_df = pd.read_excel(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(input_df)
        
# Prediction function
def predict(data):
    clf = joblib.load("model_file_best_xgb.p")
    prediction = clf.predict(data)
    probabilities = clf.predict_proba(data)
    return prediction, probabilities

# Apply model to make predictions for single input
if input_option == "Manual Input":
    st.write("""---""")
    if st.button("Click here to Predict Customer Response"):
        result, probabilities = predict(input_df)
        probability = probabilities[0][result[0]] * 100  # Get probability for the predicted class

        if result[0] == 0:
            st.subheader(f'🔴 The Customer :red[will not respond] to the offers. Probability: {probability:.2f}%')
        elif result[0] == 1:
            st.subheader(f'🟠 The Customer :orange[will partially respond] to the offers. Probability: {probability:.2f}%')
        else:
            st.subheader(f'🟢 The Customer :green[will respond] to the offers! Probability: {probability:.2f}% :smiley:')

# Mapping predictions to labels
prediction_mapping = {
    0: "No Response",
    1: "Partial Response",
    2: "Full Response"
}

# Apply model to make predictions
st.write("""---""")
if st.button("Click here to Predict Customer Response"):
    result, probabilities = predict(input_df)
    # Map predictions to their labels
    input_df['Prediction'] = [prediction_mapping[pred] for pred in result]
    # Add probability for each prediction
    input_df['Probability'] = [f"{probabilities[i][result[i]] * 100:.2f}%" for i in range(len(result))]

    # Display results
    st.write("Prediction Results:")
    st.dataframe(input_df)

    # Save DataFrame to an in-memory buffer for Excel download
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        input_df.to_excel(writer, index=False, sheet_name='Predictions')
    processed_data = output.getvalue()

    # Download button for Excel file
    st.download_button(
        label="Download Results",
        data=processed_data,
        file_name="prediction_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
