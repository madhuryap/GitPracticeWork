from selenium import webdriver
driver = webdriver.Chrome(chromePath)
driver.get(actiUrl)
cookieinfo = {"name":"xyz","value":"xyz123"}
driver.add_cookie(cookieinfo)
time.sleep(4)
print("cookie",cookieinfo,"is added")
driver.quit()