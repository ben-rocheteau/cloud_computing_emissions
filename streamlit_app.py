import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import requests
# import os
# import json
import streamlit as st
# import subprocess

custom_css = """
.css-1l02zno {
    padding-left: 15px !important;
    padding-right: 15px !important;
}
"""

# Inject custom CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

st.title("Carbon Emissions from Cloud Computing")
st.write("Hello, this is a Streamlit app for our Data Mining Project")
st.write("We are two students of the M2 - D3S at TSE")

st.markdown("<hr>", unsafe_allow_html=True)

# SideBar Configuration

st.sidebar.image('images_app/TSE_Logo_2019.png', width=300)

st.sidebar.write('Choose a GitHub Repository :')

options = ['Numpy', 'Tensorflow', 'Tidyverse']
selected_option = st.sidebar.selectbox('Sélectionnez une option', options)


# if selected_option == 'Numpy':
#   df_jobs_with_co2 = pd.read_csv('/content/cloud_computing_emissions/0_Data/tidyverse_data.csv')

# if selected_option == 'Tensorflow':
#   df_jobs_with_co2 = pd.read_csv('/content/cloud_computing_emissions/0_Data/tidyverse_data.csv')

if selected_option == 'Tidyverse':
  df_jobs_with_co2 = pd.read_csv('/content/cloud_computing_emissions/0_Data/tidyverse_data.csv')


if selected_option:

  sum_em_repo = df_jobs_with_co2['co2_emission'].sum()
  sum_em_repo = "{:.3f}".format(sum_em_repo)

  nb_runs = len(df_jobs_with_co2['run_id'].unique())

  nb_jobs = len(df_jobs_with_co2)

  mean_jobs_per_run = len(df_jobs_with_co2) // len(df_jobs_with_co2['run_id'].unique())


  col1, col2 = st.columns(2)

  # Content for the first column
  with col1:
      st.write(f"**Global KPI for the {selected_option} repository**")
      st.write(f'Total Co2 emissions : {sum_em_repo}') 
      st.write(f'Number of Runs : {nb_runs}')
      st.write(f'Number of Jobs : {nb_jobs}')
      st.write(f'Mean Number of Jobs per Run : {mean_jobs_per_run}')

  # Content for the second column
  with col2:
      st.write(f"**Carbon Emissions across time**")

      x = df_jobs_with_co2['started_at']
      y = df_jobs_with_co2['co2_emission']

      sns.set_style("whitegrid")
      fig, ax = plt.subplots()
      ax.plot(x, y)
      ax.set_xlabel('Date')
      ax.set_ylabel('Co2 Emission')
      st.pyplot(fig)