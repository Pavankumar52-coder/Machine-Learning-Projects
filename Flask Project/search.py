import streamlit as st
import pandas as pd

clustered_data = pd.read_csv('test_with_clusters.csv')
test = pd.read_csv('train_with_clusters.csv')
test_predictions = pd.read_csv('test_predictions.csv')
processed_output = pd.read_excel('output.xlsx')

processed_output['date'] = processed_output['date'].dt.strftime('%Y-%m-%d')

st.title("Machine Learning Results")

st.header("Tested Clusters Results")
st.dataframe(clustered_data)

st.header("Trained clusters results")
st.dataframe(test)

st.header("Classification Results")
st.dataframe(test_predictions)

st.header("Data Processing Results")
st.dataframe(processed_output)
