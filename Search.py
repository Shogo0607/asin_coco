from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st

with st.spinner("立ち上げ中...")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    st.success("success")