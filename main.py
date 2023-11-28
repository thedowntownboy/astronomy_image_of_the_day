import streamlit as st
import requests
import datetime


api_key = "9eES3dQFZOSWgsG85DvFjdy3swn2mDhtba0LckOb"
url = "https://api.nasa.gov/planetary/apod?" \
      "api_key=9eES3dQFZOSWgsG85DvFjdy3swn2mDhtba0LckOb"

date = datetime.date.today()

response = requests.get(url)
content = response.json()
img_content = response.content
title = content['title']
explanation = content['explanation']
image = content['url']
print(image)

#st.set_page_config(layout="wide")

st.header("Astronomy Image of the day")
# st.write(date)
st.subheader(title)
st.image(image)
st.write(explanation)

