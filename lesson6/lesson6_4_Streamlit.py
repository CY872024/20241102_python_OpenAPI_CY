import streamlit as st
import tools

'''
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
'''

sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')

## Object notation
#add_selectbox = st.sidebar.selectbox(
#    "請選擇站點名稱:",
#    sitenames 
#)

with st.sidebar:
    add_selectbox = st.selectbox(
        "請選擇站點名稱",
        sitenames
    )

    st.title(f"{add_selectbox}")