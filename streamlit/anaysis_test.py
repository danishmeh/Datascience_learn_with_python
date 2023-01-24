import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp titile
st.markdown(''' # EDA WEB APP''')
st.text("This app is developed for EDA learning")

# how to upload from pc

with st.sidebar.header("Upload your dataset from your(.csv)"):
    uploaded_file = st.sidebar.file_uploader("upload your file",type=['csv'])
    df  = sns.load_dataset('titanic')
    #  st.sidebar.markdown("[Example CV File]("is jaga par kis be tarah ka url laga saktye hain")")
    st.sidebar.markdown("[Example CV File](df)")
    
if uploaded_file is not None:
    @st.cache
    
    def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv
    df = load_csv()
    pr = ProfileReport(df,explorative=True)
    st.header("**Input DataFrame**")
    st.write(df)
    st.write('---')
    st.header('**profiling Report with pandas **')
    st_profile_report(pr)
else:
        st.info("bhai jan upload kr do file") 
        if st.button("press to use example data"):
            @st.cache
            def  load_data():
                a = pd.DataFrame(np.random.rand(100,5),columns = ['A','B','C','D','E'])
                return a 
            df = load_data()
        pr = ProfileReport(df,explorative=True)
        st.header("**Input DataFrame**")
        st.write(df)
        st.write('---')
        st.header('**profiling Report with pandas **')
        st_profile_report(pr)
            
    
    
    
    
    
    
    