import streamlit as st
import pandas as pd
import requests



urls=st.text_area(label='Enter Urls',placeholder='Enter Urls Seperated By Comma')
lines = urls.split("\n")

auth = (st.secrets['api_key1'], st.secrets['api_key2'])
url = "https://lsapi.seomoz.com/v2/url_metrics"
data = {"targets":lines}
request = requests.post(url, json=data, auth=auth)

try:
     df = pd.DataFrame((request.json()['results']))[['page', 'spam_score']]
except KeyError:
     st.error('Enter Atleast One Url')

@st.cache
def convert_df(df):
     return df.to_csv(index=False).encode('utf-8')

try:
     csv = convert_df(df)
     st.download_button(
          label="Get Spam Scores",
          data=csv,
          file_name='spam_score.csv',
          mime='text/csv',
     )
except NameError:
     st.error("Write Urls")
