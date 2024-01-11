import streamlit as st
import requests
import os



api_key = os.environ.get('SECRET_KEY')
url = f"https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"



response = requests.get(url)
content = response.json()
img_content = response.content
title = content['title']
explanation = content['explanation']
image = content['url']



# page display
st.header("Astronomy Image of the day")
st.subheader(title)
st.image(image)
st.write(explanation)

