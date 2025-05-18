import re
import time
import requests
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumwire.utils import decode

def filter_network_packet(target_url, regex):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(target_url)

        # Wait for the page to load completely
        time.sleep(10)  # Adjust the sleep time as needed

        pattern = re.compile(regex)

        for request in driver.requests:
            if request.response and pattern.search(request.url):
                full_url = request.url
                print(f"Captured URL: {full_url}")

                response = requests.get(full_url)
                return response

        print("No matching URL found.")

    finally:
        driver.quit()