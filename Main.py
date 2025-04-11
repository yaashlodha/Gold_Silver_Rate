import streamlit as st
import requests
from lxml import html
import pandas as pd
from datetime import datetime
import os

# ---------------------- Web Scraping Functions ----------------------

@st.cache_data(ttl=300)
@st.cache_data(ttl=300)
def fetch_gold_price():
    url = "https://www.goldenchennai.com/finance/gold-rate-in-tamilnadu/gold-rate-in-chennai/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch page: {response.status_code}")
    
    # DEBUG: check what HTML is being served
    st.warning("Check the HTML structure returned")
    st.code(response.text[:1000])  # Show first 1000 chars of the HTML
    
    tree = html.fromstring(response.text)
    rate_text = tree.xpath('//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[3]/text()')
    
    if rate_text:
        rate = rate_text[0].replace("INR", "").replace(",", "").strip()
        return float(rate)
    else:
        raise ValueError("Gold rate not found on the page.")


@st.cache_data(ttl=300)
def fetch_silver_price():
    url = "https://www.goldenchennai.com/finance/silver-rate-in-tamilnadu/silver-rate-in-chennai/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    tree = html.fromstring(response.text)
    rate_text = tree.xpath('//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[2]/text()')
    if rate_text:
        rate = rate_text[0].replace("INR", "").replace(",", "").strip()
        return float(rate)
    else:
        raise ValueError("Silver rate not found on the page.")

# ---------------------- UI and Calculation ----------------------

st.title("💰 Gold & Silver Price Calculator")

gold_rate = fetch_gold_price()
silver_rate = fetch_silver_price()

if gold_rate and silver_rate:
    st.info(f"Current Gold Rate: ₹{gold_rate} per gram")
    st.info(f"Current Silver Rate: ₹{silver_rate} per gram")

    gms = st.number_input("Enter the weight in grams:", min_value=0.1, step=0.1)
    metal_type = st.selectbox("Select the type of metal:", ["Gold", "Silver"]).lower()

    wasteage_or_making = 0
    price = 0

    if metal_type == "gold":
        gold_type = st.selectbox("Select the type of gold:", ["916", "22k"]).lower()

        if gold_type == "916":
            waste = st.number_input("Enter the wastage percentage:", min_value=0.0, max_value=100.0, step=0.1)
            wasteage = (waste / 100) * gms
            price = wasteage * gold_rate
            wasteage = waste
            st.success(f"Total price for {gms}g of 916 gold is ₹{price:.2f}")
        else:
            making_charges = st.number_input("Enter the making charges:", min_value=0.0, step=0.1)
            base_price = gold_rate * gms
            price = base_price + making_charges
            making = making_charges
            st.success(f"Total price for {gms}g of 22k gold is ₹{price:.2f}")

    else:
        gold_type = "N/A"
        making_charges = st.number_input("Enter the making charges:", min_value=0.0, step=0.1)
        base_price = silver_rate * gms
        price = base_price + making_charges
        making = making_charges
        st.success(f"Total price for {gms}g of silver is ₹{price:.2f}")

    # ---------------------- Submit Button and Logging ----------------------
