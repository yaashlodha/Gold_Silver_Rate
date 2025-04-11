import streamlit as st
import requests
from lxml import html

# ---------------------- Web Scraping Functions ----------------------



@st.cache_data(ttl=300)
def fetch_gold_price():
    url = "https://www.goldenchennai.com/finance/gold-rate-in-tamilnadu/gold-rate-in-chennai/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    tree = html.fromstring(response.text)

    # Extracting 22K gold price for 1 gram
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

    # Extracting 22K gold price for 1 gram
    rate_text = tree.xpath('//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[2]/text()')
    
    if rate_text:
        rate = rate_text[0].replace("INR", "").replace(",", "").strip()
        return float(rate)
    else:
        raise ValueError("Gold rate not found on the page.")
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
