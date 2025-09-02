# 💰 Gold & Silver Price Calculator  

This project is a **web application built with Streamlit** that fetches live gold and silver prices from [GoldenChennai.com](https://www.goldenchennai.com) and provides an interactive calculator to estimate jewelry costs. Users can enter the weight, select the metal type, and apply wastage or making charges to calculate the final price in real-time.  

---

## Features  

* **Live Price Scraping**: Fetches up-to-date gold and silver rates directly from GoldenChennai.com.  
* **Gold Price Calculator**: Supports both 916 gold (with wastage %) and 22k gold (with making charges).  
* **Silver Price Calculator**: Calculates silver price with making charges.  
* **Interactive Web UI**: Built with Streamlit for a clean and user-friendly experience.  
* **Caching for Speed**: Uses Streamlit caching to refresh prices every 5 minutes.  

---

## How It Works  

The application follows a simple three-step flow:  

1. **Fetch Prices**: Scrapes the current gold and silver rates from GoldenChennai.  
2. **Input Details**: User enters weight in grams, chooses gold/silver, and provides wastage or making charges.  
3. **Calculate Price**: The app applies the formulas and displays the final jewelry cost instantly.  

---

## Tech Stack  

* **Backend**  
  * Python  
  * [Requests](https://docs.python-requests.org/) for HTTP requests  
  * [lxml](https://lxml.de/) for parsing HTML with XPath  

* **Frontend**  
  * [Streamlit](https://streamlit.io/) for interactive UI  

* **Data Handling**  
  * [Pandas](https://pandas.pydata.org/) (optional for expansion)  

---

## Setup and Installation  

To run this project locally, follow these steps:  

1. **Clone the repository:**  
    ```bash
    git clone https://github.com/your-username/gold-silver-price-calculator.git
    cd gold-silver-price-calculator
    ```

2. **Create a virtual environment and install dependencies:**  
    ```bash
    # Create the environment
    python -m venv env

    # Activate it (Windows)
    .\env\Scripts\activate

    # Activate it (macOS/Linux)
    source env/bin/activate

    # Install required packages
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application:**  
    ```bash
    streamlit run app.py
    ```
    The application should now be running and accessible in your web browser.  

---

## Functions  

* **`fetch_gold_price()`**  
  * Scrapes and returns the current gold price per gram.  
  * Cleans the extracted value (removes INR, commas, spaces).  
  * Uses Streamlit caching (5 minutes).  

* **`fetch_silver_price()`**  
  * Scrapes and returns the current silver price per gram.  
  * Cleans the extracted value.  
  * Uses Streamlit caching (5 minutes).  

---

## Future Improvements  

* **Add More Gold Types**: Support for 18k and 24k calculations.  
* **Multi-City Support**: Fetch rates from multiple cities, not just Chennai.  
* **Graphical Trends**: Display historical price trends with charts.  
* **Export Options**: Allow users to download calculation results as PDF or Excel.  
