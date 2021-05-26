#Creator: github/darth_data
#Created: 25May2021 15:05

#This application needs to run using Streamlit, to run type 'streamlit app.py' on command line

import streamlit as st
import numpy as np
import plotly.express as px

# list_1 = np.linspace(5, 25, 5)
# sidebar_1 = st.sidebar.selectbox()
# sidebar_1 = st.sidebar.slider('Some value 1',5, 150, (5, 50))
# sidebar_2 = st.sidebar.slider('Some value 2',0,150,(20,100))
# sidebar_3 = st.sidebar.selectbox('Number of price points to create', list_1)

values = ['<select>','wind','iris','carshare','gapminder','tips','election']
default_ix = values.index('<select>')
data_option = st.sidebar.selectbox('Which dataset ?: ',values,index=default_ix)



st.write("Let's visualise __"+data_option+"__ data!")





def choose_data():
    if data_option == "wind":
        df = px.data.wind()
        fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark",
            color_discrete_sequence= px.colors.sequential.Plasma_r)
       

    elif data_option == "iris":
        df = px.data.iris()
        fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

    elif data_option == "gapminder":
        df = px.data.gapminder().query("year == 2007")
        fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'])
    
    elif data_option == "tips":
        df = px.data.tips()
        fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df.columns)

    elif data_option == "election":
        df = px.data.election()
        fig = px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total", hover_name="district",
                  symbol="result", color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"})
    else:
        df = px.data.carshare()
        fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")
                #   mapbox_style="open-street-map")
    st.write(fig)
    st.write("Sample data:")
    st.write(df)
       
choose_data()



##Alternative approach


# def choose_data():
#     if data_option == "wind":
#         df = px.data.wind()
#         fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark",
#             color_discrete_sequence= px.colors.sequential.Plasma_r)
#         table_graph(df,fig)
        

#     elif data_option == "iris":
#         df = px.data.iris()
#         fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
#         table_graph(df,fig)
        
#     else:
#         df = px.data.carshare()
#         fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
#                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                   mapbox_style="carto-positron")
#                 #   mapbox_style="open-street-map")
#         table_graph(df,fig)
        

# def table_graph(df,fig):
#     st.write(df)
#     st.write("Sample data:")
#     st.write(fig)


# choose_data()