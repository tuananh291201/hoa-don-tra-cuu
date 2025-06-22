from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def read_invoice_code_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readline().strip()

def open_website(driver, url):
    driver.get(url)
    time.sleep(1)

def enter_invoice_code(driver, code):
    input_box = driver.find_element(By.ID, "txtCode")
    input_box.clear()
    input_box.send_keys(code)
    time.sleep(1)

def search_invoice(driver):
    driver.find_element(By.ID, "btnSearchInvoice").click()
    time.sleep(3)

def download_invoice_as_pdf(driver):
    try:
        driver.find_element(By.CLASS_NAME, "res-btn.download").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[contains(@class,'txt-download-pdf')]").click()
        print("Đã nhấn tải PDF.")
    except Exception as e:
        print("Không tìm thấy tuỳ chọn tải PDF:", e)

def main():
    invoice_code = read_invoice_code_from_txt("input/ma_tra_cuu.txt")
    driver = webdriver.Chrome()
    try:
        open_website(driver, "https://www.meinvoice.vn/tra-cuu")
        enter_invoice_code(driver, invoice_code)
        search_invoice(driver)
        download_invoice_as_pdf(driver)
        time.sleep(10)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
