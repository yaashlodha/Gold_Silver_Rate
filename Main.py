import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
def get_headless_driver():
    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode

    service = Service()  # Or provide the path to your chromedriver here
    driver = webdriver.Chrome(service=service, options=options)
    return driver



# Cache gold price to avoid multiple fetches
@st.cache_data
def fetch_gold_price():
    driver = get_headless_driver()
    driver.get("https://www.goldenchennai.com/finance/gold-rate-in-tamilnadu/gold-rate-in-chennai/")
    time.sleep(5)
    try:
        element = driver.find_element(By.XPATH, '//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[3]')
        rate = element.text.replace('INR', '').replace(' ', '').replace(',', '')
        return float(rate)
    except Exception as e:
        st.error(f"Failed to fetch gold rate: {e}")
        return None
    finally:
        driver.quit()

# Cache silver price to avoid multiple fetches
@st.cache_data
def fetch_silver_price():
     
    driver = get_headless_driver()
    driver.get("https://www.goldenchennai.com/finance/silver-rate-in-tamilnadu/silver-rate-in-chennai/")
    time.sleep(5)
    try:
        element = driver.find_element(By.XPATH, '//table[contains(@class,"table-db")][1]/tbody/tr[2]/td[2]')
        rate = element.text.replace('INR', '').replace(' ', '').replace(',', '')
        return float(rate)
    except Exception as e:
        st.error(f"Failed to fetch silver rate: {e}")
        return None
    finally:
        driver.quit()

# Helper functions
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

st.title("Gold & Silver Price Calculator")

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
