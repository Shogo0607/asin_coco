from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import streamlit as st
with st.spinner("立ち上げ中..."):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')  
    chrome_options.add_argument('--disable-dev-shm-usage') 
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    print('>処理開始')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    st.success("success")