#from fastai2.vision.all import open_image, load_learner, image, torch
#import torch
from fastai.vision import *
from fastai import *
import streamlit as st
from PIL import Image
from pathlib import Path
import json



st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("RECONOCIMIENTO DE MARIPOSAS - API")

introduction_str = 'Este es un clasificador de imagenes de mariposas  '

st.markdown(introduction_str)

# Loading Model
path_file = Path('.','modelo_mariposas.pkl')
butterfly_classifier = load_learner(path_file )


# load Wikipedia dictionaries info
   

# Loading File to classify

file_up = st.file_uploader(
    "Subir una imagen de mariposas", 
    type=['png', 'jpg', 'jpeg'])

#try:
#    image = Image.open(file_up)
#    st.image(image, caption='Uploaded Image.', use_column_width=True)
#except:
#    st.write("No files upload")



if file_up is not None: 
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

#    butterfly_classifier = torch.load('modelo_mariposas.pkl')
    image = PILImage.create(file_up)
    pred,pred_idx,probs = butterfly_classifier.predict(image)

    st.subheader("Fish Specie Prediction")
    out_label = f'Predicion: {pred}; Clase: {pred_idx}'

    st.write(out_label)
    st.markdown("\n\n")
 


    # Wikipedia data



#from fastai2.vision.all import *
#from fastai2.vision.widgets import *



#inferencer = load_learner(path)

#img_bytes = st.file_uploader("Squash It!!", type=['png', 'jpg', 'jpeg'])
#if img_bytes is not None:
#    st.write("Image Uploaded Successfully:")
#    img = PIL.Image.open(img_bytes)

#    pred_class, pred_idx, outputs = inferencer.predict(img)
#    for out in outputs:
#        st.write(out)

#    st.write("Decision: ", pred_class)
