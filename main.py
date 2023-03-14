from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_data_from_whatsapp_group():
    """
    Extracts data from whatsapp group to a csv file
    return: None
    """

    # Replace with the path of your chromedriver executable
    driver = webdriver.Firefox()

    # Load WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Wait for the user to scan the QR code
    input("Scan the QR code and press any key to continue...")

    # Find the group chat by its title
    chat_title = "כסף מהחתונה"
    wait = WebDriverWait(driver, 10)
    chat = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//span[@title='{chat_title}']")))

    chat.click()

    # Find all the messages in the chat
    messages = driver.find_elements(By.XPATH, "//div[@class='copyable-text']")

    # Print each message
    for message in messages:
        print(message.text)

    # Close the browser
    driver.quit()

if __name__ == '__main__':
    extract_data_from_whatsapp_group()