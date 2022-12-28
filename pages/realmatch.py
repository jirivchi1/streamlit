import streamlit as st
import os

import pandas as pd

from PIL import Image



picture = st.camera_input("Es hora de la foto")

if picture:
    st.image(picture)

if picture is not None:
    with open(picture.name,'wb') as f:
        f.write(picture.getbuffer())

    st.success('Imagen Guardada')