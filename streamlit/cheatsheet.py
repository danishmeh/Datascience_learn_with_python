import streamlit as st 
import seaborn as sns




st.header("add header and Italic")
'_This_ is _some_ **Markdown**'
'dataframe:'

st.header("How to add Calendar")
st.date_input("enter date")

st.header("simple text")
st.text('Fixed width text')
st.markdown('**_Markdown_**')
st.title('This is Title ')
st.header('This is the first heading')
st.subheader('This is the second heading')


st.header("Create a Button")
st.button('Click me')
st.header("Add Checkbox")
st.checkbox("Agree")
st.checkbox("Not Agree")
st.header("pick one")
st.radio("pick one",['Instrument','Electronics','Electrical','Computer'])
st.selectbox("choose",["A","B","C","D","E","F","G","H","I"])
st.selectbox('Pick one', ['Danish', 'Ahtisam'])
st.slider("pick a vaku",0,100,value=10,step=5)
st.select_slider("shirt Size",['Small','Medium','Large'],value='Medium')
st.text_input("what is your name?")
st.text_input("What is your father name")
st.text_input("What is your mother")
st.text_input("What is your age")
st.time_input("What is time now")
# st.camera_input("photo Smile")
st.color_picker('color Pick')
my_dataframe =sns.load_dataset('iris')
st.dataframe(my_dataframe.head(1))
st.header("Columns")
col1,col2 = st.columns(2)
col1.write("this is first column")
col2.write("this is second column")
first_name,last_name = st.columns(2)
first_name.write("1st")
last_name.write("2nd")
with col1:
    st.radio('Select one:', [1, 2])

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
    # st.balloons()
    # st.snow()
st.error('Error message')
st.warning('Warning message')
st.success('Success message')













