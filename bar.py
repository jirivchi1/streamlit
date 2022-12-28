import streamlit as st
import pandas as pd
import numpy as np


dict1 = {'Tapas':['Carne','Berengenas','Bravas'], 'Bebidas':['Tinto', 'Cerveza','Cola']}

df = pd.DataFrame(dict1)

tapa = st.selectbox('¿Qué tapa desea?', df['Tapas'])

bebida = st.selectbox('¿Qué bebida desea?', df['Bebidas'])

'Resumen pedido: ', tapa, bebida





