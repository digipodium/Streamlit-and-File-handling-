import streamlit as st
import pandas as pd
from PIL import Image
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.title("uploading files in streamlit")
st.subheader('into project folder and database')

options= ['upload image','upload text file', 'upload any file']
ch = st.selectbox("choose",options)
if ch =='upload image':
    img = st.file_uploader('select image',type=['jpg','png'])
    if img:
        name= os.path.splitext(img.name)[0]
        ext = img.type.split('/')[1]
        path = os.path.join('uploads',f'{img.name}')
        im =  Image.open(img)
        im.save(path,format=ext) # store in upload
        st.image(im)
if ch =='upload text file':
    file = st.file_uploader('select image',type=['txt','doc','pdf'])
    if file:
        path = os.path.join('uploads',f'{file.name}')
        with open(path,'wb') as f:
            f.write(file.getbuffer())
            st.success("file uploaded successfully")

if ch =='upload any file':
    
    file = st.file_uploader('select image',type=['mp4','avi','webm','mp3'])
    if file:
        path = os.path.join('uploads',f'{file.name}')
        with open(path,'wb') as f:
            f.write(file.getbuffer())
            st.success("file uploaded successfully")