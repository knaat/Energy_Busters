import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import altair as alt

# Set wide page mode
st.set_page_config(layout="wide")

#Read image and decorate with streamlit cache function to avoid reloading each time script executes:
@st.cache
def load_grid_image():
    grid = plt.imread('grid.jpg')
    return grid

grid = load_grid_image()

# Now start building up the display with some titles.
st.title('Energy Busters -  Energy Transition Predictor')

# Radio selector om een scherm te kiezen
screen = st.sidebar.radio('Selecteer het scherm', ['Project plaatsing'])

screen1=False
screen2=False
screen3=False

if screen == 'Project plaatsing':
    screen1=True
elif screen == 'Scherm 2':
    screen2=True
elif screen == 'Scherm 3':   
    screen3=True

if screen1:

    # Display some headers
    st.header('Screen 1: Project plaatsing')
    st.sidebar.header('Project plaatsen')

    # Define 2 columns with a dummy 'spacer column for better layout (column object is in beta) 
    c1, dum, c2 = st.beta_columns((10,1,10))

    c1.subheader('Grid kaart')
    c2.subheader('Details')

    x1 = st.sidebar.slider('Selecteer de X-positie van het project', 0, 513, 250, 1)
    y1_min = 0
    y1_max = 540
   
    y2 = st.sidebar.slider('Selecteer de Y-positie van het project', 0, 540, 250, 2)
    x2_min = 0
    x2_max = 513


    fig, ax = plt.subplots()
    ax.imshow(grid, extent=[0, 513, 0, 540])

    x = [x1,x1]
    y = [y1_min, y1_max]
    ax.plot(x, y, '--', linewidth=1, color='blue')

    x = [x2_min,x2_max]
    y = [y2, y2]
    ax.plot(x, y, '--', linewidth=1, color='blue')

    # Radio selector om een scherm te kiezen
    type = st.sidebar.radio('Selecteer type project', ['Wind', 'Zon'])
    power = st.sidebar.slider('Selecteer vermogen van het project in Megawatt', 0, 100, 50, 5)

    if type == 'Wind':
        color='c'
    elif type == 'Zon':
        color='r'
    else:
        Print(f'Invalid choice of type {type}')

    cir = plt.Circle((x1, y2), power/5, color=color,fill=True)
    ax.add_patch(cir)

    c1.pyplot(fig)

