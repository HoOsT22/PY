from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/watch?v=VjGt3EfgwAY")

print(driver.title)

driver.close()