import streamlit as st
import pandas as pd
import requests



urls=st.text_area(label='Enter Urls',placeholder='Enter Urls Seperated By Comma')


auth = ('mozscape-b4a2d301dd', '9e00ec0901b395044bc485fef2215fe3')
url = "https://lsapi.seomoz.com/v2/url_metrics"
data = {"targets":urls.split(',')}
request = requests.post(url, json=data, auth=auth)

try:
     df = pd.DataFrame((request.json()['results']))[['page', 'spam_score']]
except KeyError:
     st.error('Enter Atleast One Url')

button = st.button('SaveFile')
if button:
     df.to_csv('spam_score.csv', index=False)


# uploaded_file = st.file_uploader("Choose a file",type=['txt'])
# if uploaded_file is not None:
#      # To read file as bytes:
#      bytes_data = uploaded_file.getvalue()
#
#      st.write(bytes_data.decode('utf-8'))
#
#      auth = ('mozscape-b4a2d301dd', '9e00ec0901b395044bc485fef2215fe3')
#      url = "https://lsapi.seomoz.com/v2/url_metrics"
#      request = requests.post(url, data=bytes_data.decode('utf-8'), auth=auth)
#
#      df=pd.DataFrame((request.json()['results']))[['page','spam_score']]
#
#      button=st.button('SaveFile')
#
#      if button:
#           df.to_csv('spam_score.csv',index=False)