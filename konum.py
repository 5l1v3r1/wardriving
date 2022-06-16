#html5 kullanılarak konum bilgisi tek seferlik aktif edilmesi ile anlık konum bilgileri sürekli elde edilmiştir.
from selenium import webdriver
import time
import datetime
driver = webdriver.Firefox()
driver.get("https://www.geody.com")
driver.find_element_by_id("cookieChoiceDismiss").click()
while 1:
    driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[1]/a").click()
    time.sleep(10)
    konum=str(driver.current_url).split("&")[1:]
    print konum
    log=str(konum[0])+"|"+str(konum[1])+"|"+str(datetime.datetime.now().strftime("%d %B %Y %I:%M%p"))+"\n"
    dosya=open("konum.txt","a")
    dosya.write(log)
    dosya.close()
    driver.refresh()
