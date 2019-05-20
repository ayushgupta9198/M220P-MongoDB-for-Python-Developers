from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='C:\\Users\\Prince\\Downloads\\chromedriver.exe')
driver.get('https://www.justdial.com/')
driver.find_element_by_id('srchbx').send_keys('Restaurants')
driver.find_element_by_xpath('//*[@id="search"]/button').click()
# elements=driver.find_element_by_class_name('col-sm-5 col-xs-8 store-details sp-detail paddingR0')
# url=driver.find_elements_by_class_name('contact-info')
a={'dc':'+','fe':'(','hg':')','ba':'-','acb':0,'yz':1,'wx':2,'vu':3,'ts':4,'rq':5,'po':6,'nm':7,'lk':8,'ji':9}
out=[]
for cnt_info in driver.find_elements_by_class_name('contact-info'):
    innrdiv= cnt_info.find_element_by_tag_name('a')
    imt_out=[]
    for txt in innrdiv.find_elements_by_tag_name('span'):
        smbl=txt.get_attribute('class').split('-')[-1]
        nmbr=a[smbl]
        imt_out.append(str(nmbr))
    print(''.join(imt_out))
    out.append(''.join(imt_out))

print(out)


    # i=+1
    # a_tag = links.find_element_by_tag_name("span")
    # nmbrs = a_tag.find_elements_by_tag_name("a")
    # for nmbr in nmbrs.find_elements_by_tag_name()
# print(url1)





# var1=driver.find_elements_by_class_name('contact-info')
# var2=driver.find_element_by_tag_name('<b>')
# print(var2.text)
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="setbackfix"]/section[1]/section[2]/section/div[2]/div/div[2]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="setbackfix"]/section[1]/section[2]/section/div[2]/div/div[2]').click()
# driver.find_element_by_xpath('//*[@id="setbackfix"]/section[1]/section[2]/section/div[2]/div/div[2]').send_keys('Restaurant')

