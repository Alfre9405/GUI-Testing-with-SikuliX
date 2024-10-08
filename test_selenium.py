from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the ChromeDriver service
service = Service('C:/chromedriver-win64/chromedriver.exe')

# 1.Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# 2.Open the URL
driver.get("https://www.adidas.com/us/")
driver.maximize_window()

# Wait until the page fully loads
wait = WebDriverWait(driver, 10)

try:
    # 3. Find and click on the search bar
    search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))  # Adjust this
    search_box.click()
    
    # 4. Type "mens sneakers" and press enter
    search_box.send_keys("mens sneakers" + Keys.ENTER)

    # 5. Scroll down and click on the image using XPath
    product_image_xpath = '//*[@id="__next"]/div[2]/main/section[2]/article[8]/div/header/a'
    product_image = wait.until(EC.element_to_be_clickable((By.XPATH, product_image_xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", product_image)  # Scroll to the image
    time.sleep(1)  # Wait a second for the image to be visible
    product_image.click()  # Click on the image

    # 6. Wait for the new page to load
    time.sleep(5)  # Adjust this time as needed

    # 7. Scroll down and select the size
    size_button_xpath = '//*[@id="main-content"]/div[2]/div[2]/section/div[1]/div[2]/button[17]/span'
    size_button = wait.until(EC.element_to_be_clickable((By.XPATH, size_button_xpath)))
    time.sleep(1)  # Wait a second for the button to be visible
    size_button.click()  # Click on the size button

    # 8. Scroll down and click the "Add To Bag" button
    add_to_bag_button_xpath = '//*[@id="add-to-bag"]/button'
    add_to_bag_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_bag_button_xpath)))
    
    driver.execute_script("arguments[0].scrollIntoView();", add_to_bag_button)  # Scroll to the "Add To Bag" button
    time.sleep(1)  # Wait a second for the button to be visible
    add_to_bag_button.click()  # Click on the "Add To Bag" button

    # 9.Check if the modal window has populated
    modal_header_xpath = '//*[@id="modal-root"]/div[2]/div/div/div[2]/h5'
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, modal_header_xpath)))
        print("The modal window has populated successfully.")
    except:
        print("The modal window did not populate, clicking 'Add To Bag' again.")
        add_to_bag_button.click()  # Click the button again

    # Wait a moment to see the results (optional)
    time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

# Close the driver at the end
driver.quit()



