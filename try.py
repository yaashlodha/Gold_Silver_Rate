from lxml import html
import requests
import streamlit as st

@st.cache_data(ttl=300)
def fetch_gold_price():
    url = "https://www.goldenchennai.com/finance/gold-rate-in-tamilnadu/gold-rate-in-chennai/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    tree = html.fromstring(response.text)

    # Extracting 22K gold price for 1 gram
    rate_text = tree.xpath('//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[2]/text()')
    
    if rate_text:
        rate = rate_text[0].replace("INR", "").replace(",", "").strip()
        return float(rate)
    else:
        raise ValueError("Gold rate not found on the page.")
a= fetch_gold_price()
st.write(a)