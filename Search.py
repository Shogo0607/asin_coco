from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st
with st.spinner("立ち上げ中..."):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    st.success("success")