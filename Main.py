import streamlit as st
import requests
from lxml import html

# ---------------------- Web Scraping Functions ----------------------

@st.cache_data

def fetch_gold_price():
    try:
        url = "https://www.goldenchennai.com/finance/gold-rate-in-tamilnadu/gold-rate-in-chennai/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        response = requests.get(url, headers=headers)
        tree = html.fromstring(response.content)
        rate_list = tree.xpath('//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[2]')
        
        if rate_list:
            rate = rate_list[0].text_content().replace('INR', '').replace(' ', '').replace(',', '')
            return float(rate)
        else:
            raise ValueError("gold rate not found in HTML")
    
    except Exception as e:
        st.warning(f"Failed to fetch gold rate: {e}")
        return None

@st.cache_data

def fetch_silver_price():
    try:
        url = "https://www.goldenchennai.com/finance/silver-rate-in-tamilnadu/silver-rate-in-chennai/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        response = requests.get(url, headers=headers)
        tree = html.fromstring(response.content)
        rate_list = tree.xpath('//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[2]')
        
        if rate_list:
            rate = rate_list[0].text_content().replace('INR', '').replace(' ', '').replace(',', '')
            return float(rate)
        else:
            raise ValueError("Silver rate not found in HTML")
    
    except Exception as e:
        st.warning(f"Failed to fetch silver rate: {e}")
        return None

# ---------------------- Helper Functions ----------------------

def check_make_charges(rate):
    if rate < 2000:
        return 200
    elif 2000 <= rate < 5000:
        return 500
    elif rate >= 5000:
        return 1000
    return 0

def wastage_calculate_price(gms, rate):
    base_price = gms * rate
    return base_price + ((base_price * 10) / 100)

def making_calculate_price(gms, rate):
    base_price = gms * rate
    return base_price + check_make_charges(base_price)

# ---------------------- Streamlit App ----------------------

st.title("💰 Gold & Silver Price Calculator")

gold_rate = fetch_gold_price()
silver_rate = fetch_silver_price()

if gold_rate and silver_rate:
    st.info(f"Current Gold Rate: ₹{gold_rate} per gram")
    st.info(f"Current Silver Rate: ₹{silver_rate} per gram")

    gms = st.number_input("Enter the weight in grams:", min_value=0.1, step=0.1)

    metal_type = st.selectbox("Select the type of metal:", ["Gold", "Silver"]).lower()

    if metal_type == "gold":
        gold_type = st.selectbox("Select the type of gold:", ["916", "22k"]).lower()
        if gold_type == "916":
            price = wastage_calculate_price(gms, gold_rate)
            st.success(f"Total price for {gms}g of 916 gold is ₹{price:.2f}")
        else:
            price = making_calculate_price(gms, gold_rate)
            st.success(f"Total price for {gms}g of 22k gold is ₹{price:.2f}")
    else:
        price = making_calculate_price(gms, silver_rate)
        st.success(f"Total price for {gms}g of silver is ₹{price:.2f}")
else:
    st.warning("Unable to fetch live prices. Please try again later.")
