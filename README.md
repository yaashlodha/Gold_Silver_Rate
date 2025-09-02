Gold & Silver Price Calculator

This is a Streamlit web application that fetches live gold and silver rates from GoldenChennai.com
 and provides an interactive calculator to estimate the total cost of jewelry based on weight, type of metal, and additional charges.

🚀 Features

Live gold and silver prices (cached for 5 minutes).

Supports both 916 gold (with wastage percentage) and 22k gold (with making charges).

Calculates silver price with making charges.

Clean and interactive user interface built with Streamlit.

📦 Requirements

Python 3.8+

Install dependencies:

pip install streamlit requests lxml pandas

▶️ Usage

Run the app with:

streamlit run app.py


(replace app.py with the filename).

🧮 Example

Current gold rate: ₹5,700/g

Input: 10g of 916 gold with 5% wastage

Calculation: (10 + 0.5) × 5700 = ₹59,850

📌 Notes

Prices are scraped from GoldenChennai.com and may change based on website structure.

Cache refreshes every 5 minutes to reduce load time.
