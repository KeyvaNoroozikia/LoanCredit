# -*- coding: utf-8 -*-
"""Streamlit_front.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Se8zT5JTOKsVzsMyQZdyDjsMevDvr01C

# Application Streamlit via Google Colab:

On va mettre en place notre application et notre dashboard via Streamlit, sur lequel on va appliquer notre modèle LightGBM.
"""

#pip install  pyngrok

#pip install  streamlit

#!pip install -q streamlit_ace

#pip install shap

import streamlit as st
import pandas as pd
import base64
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import MinMaxScaler
import numpy as np
#import pickle as pkl
#import shap
import streamlit.components.v1 as components

"""## Mise en place de l'application Streamlit : paramétrage

"""

#!pip install pyngrok
#!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import pandas as pd
# import pickle
# import streamlit as st
# import json 
# import numpy as np
# import shap
# 
# 
# 
# 
# st.set_page_config(
#     page_title="Loan Prediction App by Keyvan NOROOZI KIA",
# 
# )
# 
# st.set_option('deprecation.showPyplotGlobalUse', False)
# 
# ######################
# #main page layout
# ######################
# import requests as re
# 
# st.title("Credit Card Fraud Detection Web App")
# 
# 
# st.write("""
# ## About
# This app is created by Alex Noroozi Kia. It predicts if a customer will be able, or no, to 
# refund his loan.
# """)
# 
# 
# st.sidebar.header('Input Features of The Transaction')
# 
# first_name = st.sidebar.text_input("""Input first name """)
# last_name = st.sidebar.text_input("""Input last name""")
# name_contract_type = st.sidebar.number_input("Contract product type (Cash loan, consumer loan [POS]) of the previous application: Type 0 for a cash loan or 1 for a revolving loan",min_value=0, max_value=3)
# children_count = st.sidebar.number_input("how many children do you have?",min_value=0, max_value=11)
# fam_members = st.sidebar.number_input("how many family members do you have",min_value=0, max_value=15)
# 
#     
# amt_credit_sum = st.sidebar.number_input("What is the amount of credit you want?",min_value=0, max_value=110000)
# DAYS_INSTALMENT_delay = st.sidebar.number_input("""delay since your last credit?""",min_value=0, max_value=1000)
# amt_income_total= st.sidebar.number_input("""Income per year?""",min_value=0, max_value=11000000)
# credit_active= st.sidebar.number_input("""Credit active? put 0 if you don't have any info, 1 if the Credit's closed, 2 if the Credit is active and 3 if it has been sold """,min_value=0, max_value=3)
# bureau_year= st.sidebar.number_input("""bureau_year : Number of enquiries to Credit Bureau about the client one day year (excluding last 3 months before application)""",min_value=0, max_value=20)
# 
# 
# if st.button("Detection Result"):
#     values = {
#     "name_contract_type": name_contract_type,
#     "children_count": children_count,
#     "fam_members": fam_members,
#     "credit_active": credit_active,
#     "amt_income_total": amt_income_total,
#     "DAYS_INSTALMENT_delay": DAYS_INSTALMENT_delay,
#     "amt_credit_sum": amt_credit_sum,
#     "bureau_year":bureau_year
#     }
# 
# 
# 
#     res = re.post(f"https://194d-35-204-42-152.ngrok.io/predict",json=values)
#     json_str = json.dumps(res.json())
#     resp = json.loads(json_str)
#     
#     if first_name=='' or last_name == '':
#         st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
#     else:
#         st.write(f"{resp[0]}")
#     
#

"""## Installation du tunnel local"""

#!npm install -g localtunnel

"""## Exécution de Streamlit sur colab

"""

#!streamlit run /content/app.py &>/content/logs.txt &

"""
## Mise en place du tunnel sur le port 8501
Then just click in the `url` showed.

A `log.txt`file will be created."""

#!npx localtunnel --port 8501

"""[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y3VYYE)"""
