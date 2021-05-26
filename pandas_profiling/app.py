import pandas as pd
import pandas_profiling
import xlrd
import sys
import datetime
import os
import json
from openpyxl import Workbook

from typing import Dict

if sys.version_info[0] < 3: 
    from StringIO import StringIO # Python 2.x
else:
    from io import StringIO # Python 3.x


import streamlit as st

from streamlit_pandas_profiling import st_profile_report

# df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
# pr = df.profile_report()

# st_profile_report(pr)
# st.write(sys.version_info[0])

values = ['<select>','csv','xlsx','txt']
default_ix = values.index('<select>')
# file_option = st.selectbox('Select filetype: ',('<select>','csv','xls','txt'),index=default_ix)
file_option = st.selectbox('What kind of file? ',values,index=default_ix)

delim = ','

result = st.file_uploader("Upload", type=file_option)

@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """this dictionary initialised once and can store uploaded files info"""
    return {}

def showData():
    """Function to show the data"""
    static_store = get_static_store()

    # st.info(__doc__)
    
    if result:
        # Process you file here
        value = result.getvalue()

        # And add it to the static_store if not already in
        if not value in static_store.values():
            static_store[result] = value
    else:
        static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
        # st.info("Upload one or more  files.")

    if st.button("Clear file list"):
        static_store.clear()

    if st.checkbox("Preview file and choose columns"):
        if file_option == 'csv':
            df = pd.read_csv(result, sep = delim, encoding = 'utf-8', error_bad_lines=False)
            
            ts = datetime.datetime.now()
            df['Modified timestamp'] = ts
            # st.dataframe(df)
        else:
            csv_string = result.read()
            df = pd.read_csv(StringIO(csv_string),encoding = 'utf-8', delimiter = '\t', header = 1)
            
            ts = datetime.datetime.now()
            df['Modified timestamp'] = ts
            
        filtered = st.multiselect('Columns: ', options = list(df.columns), default = list(df.columns) )
        
        st.write(df[filtered])


def uploadData():
    
    static_store = get_static_store()

    # st.info(__doc__)
    
    if result:
        # Process you file here
        value = result.getvalue()

        # And add it to the static_store if not already in
        if not value in static_store.values():
            static_store[result] = value
    else:
        static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
        # st.info("Upload one or more  files.")

    # if st.button("Clear file list"):
    #     static_store.clear()

    if st.checkbox("Preview file and choose columns"):
        if file_option == 'csv':
            df = pd.read_csv(result, sep = delim, encoding = 'utf-8', error_bad_lines=False)
            
            ts = datetime.datetime.now()
            df['Modified timestamp'] = ts
            # st.dataframe(df)
        elif file_option == 'xlsx':
            df = pd.read_excel(result, index_col=0, engine = 'openpyxl')


        else:
            csv_string = result.read()
            df = pd.read_csv(StringIO(csv_string),encoding = 'utf-8', delimiter = '\t', header = 0)
            
            ts = datetime.datetime.now()
            df['Modified timestamp'] = ts
            
        filtered = st.multiselect('Columns: ', options = list(df.columns), default = list(df.columns) )
        df = df[filtered]
        st.write(df)

        if st.button('Pimp my data!'):
            
            import time
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)

            # df.reset_index(inplace = True)
            # df_dict = df.to_dict('records')
            # collection.insert_many(df_dict)
            # df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
            pr = df.profile_report()

            st_profile_report(pr)


            st.balloons()

            st.write("We've analysed your data!")

uploadData()