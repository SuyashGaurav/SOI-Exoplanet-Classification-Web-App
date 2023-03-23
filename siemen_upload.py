import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import pickle
from xgboost import XGBClassifier
import plotly.express as px
from PIL import Image


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")


animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.write("""
# Exoplanet Prediction App
""")
st.sidebar.header('User Input')

st.subheader("Training data")
tce_data=pd.read_csv("problem_dataset.csv")
st.write(tce_data)
st.write("Accuracy of the model:- 83.1029 %")
image = Image.open('confusion matrix.png')
st.image(image, caption = 'Confusion matrix of the model')


uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    tce_data1 = input_df
    X_test2 =tce_data1.drop(['kepid', 'tce_plnt_num', 'tce_insol', 'tce_insol_err', 'tce_rogue_flag'], axis =1)

    st.subheader("Input Data")
    st.write(tce_data1)

    load_model= pickle.load(open("siemen.pkl",'rb'))
    y_result=load_model.predict(X_test2)

    st.subheader('Prediction')
    av_result=pd.DataFrame(y_result, columns=['av_result'])
    av_result["av_result"]= av_result["av_result"].replace([0,1,2],['AFP', 'NTP', 'PC'] )
    Result= pd.concat([tce_data1,av_result],axis=1)
    Result1= Result.drop(['tce_insol', 'tce_insol_err', 'tce_rogue_flag','tce_plnt_num', 'tce_period', 'tce_period_err', 'tce_time0bk',
           'tce_time0bk_err', 'tce_impact', 'tce_impact_err', 'tce_duration',
           'tce_duration_err', 'tce_depth', 'tce_depth_err', 'tce_model_snr',
           'tce_prad', 'tce_prad_err', 'tce_eqt', 'tce_eqt_err', 'tce_steff',
           'tce_steff_err', 'tce_slogg', 'tce_slogg_err', 'tce_sradius',
           'tce_sradius_err'],axis=1,inplace=False)
    st.write(Result1)

    st.subheader("% of different predictions")
    Result1.av_result.value_counts().plot(kind='pie', autopct = '%1.1f%%')
    st.pyplot()

    Result1 = Result1.to_csv().encode('utf-8')
    st.sidebar.header('Predicted data (csv)')
    st.sidebar.download_button(
        label = "Download",
        data = Result1,
        file_name = 'siemen_predicted_data.csv',
        mime='text/csv'
    )
