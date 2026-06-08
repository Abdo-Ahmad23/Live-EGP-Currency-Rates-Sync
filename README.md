# Odoo 17 Live Currency Rates Sync (EGP Base)

A lightweight and efficient Odoo 17 module designed to automatically synchronize and update live currency exchange rates (USD, EUR, SAR) against the Egyptian Pound (EGP) using the **ExchangeRate-API**.

## 🚀 Features
* **Automated Daily Sync:** Integrated with Odoo Scheduled Actions (Cron) to fetch rates every day at 06:00 AM Cairo Time (03:00 AM UTC).
* **Defensive Rate Management:** Automatically checks if a rate record exists for the current day to update it, preventing duplicate records for the same date.
* **Multi-Company Safe:** Correctly assigns currency rates to the active company context.
* **Clean Architecture:** Inherits directly from `res.currency` keeping the database clean without unnecessary third-party tables or overhead.

## 🛠️ Requirements & Technical Stack
* **Odoo Version:** 17.0 (Community & Enterprise)
* **Python Libraries:** `requests` (Standard Odoo dependency)
* **External API:** [ExchangeRate-API](https://www.exchangerate-api.com/)

## 📦 Installation

1. Clone or copy this repository into your Odoo custom addons directory:
   ```bash
   git clone https://github.com/Abdo-Ahmad23/Live-EGP-Currency-Rates-Sync

2. Restart your Odoo server and update the app list.

3. Install the module via CLI or from the Apps Dashboard:
        ./odoo-bin -c odoo.conf -i test_currency_sync

⚙️ Configuration & Usage

1. API Key Setup: Open models/res_currency.py and replace "YOUR_FREE_API_KEY_HERE" with your actual token from ExchangeRate-API.
2. Scheduled Action:

    Go to Settings > Technical > Automation > Scheduled Actions.
    
    Search for "ExchangeRate-API: Sync Live EGP Rates".
    
    Here you can monitor the next execution time or trigger it manually by clicking "Run Manually".
