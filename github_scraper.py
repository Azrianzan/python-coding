from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# cdp  is acronym for Chrome webDriver Path
#cdp = "C:\\Users\\Azrianzan\\Documents\\Coding\\chromedriver_win32\\chromedriver.exe"
# https://www.tokopedia.com/rogsstoreid/laptop-hp-14-intel-core-i5-1155g7-ram-16gb-512gb-ssd-14-fhd-ips-standard-16gb-512gb-ssd?extParam=ivf%3Dfalse%26src%3Dsearch

github_page = input("What is the Github page would you like to scrape? ")

def go_to_the_repo():
    for repoLink in repositories_link:
        driver.get(repoLink)
        files = driver.find_elements(By.CLASS_NAME, "Link--primary")
        files_content = driver.execute_script("""
            var contents = [];
            var elements = arguments[0];
            for (var i = 0; i < elements.length; i++) {
                contents.push(elements[i].textContent);
            }
            return contents
        """, files)
        files_links = []
        for i in files_content:
            if ".py" in i:
                files_links.append(i)
            elif ".js" in i:
                files_links.append(i)
            elif ".html" in i:
                files_links.append(i)
            elif ".css" in i:
                files_links.append(i)
            else:
                pass
            
        def open_file_and_search_password():
            for link in files_links:
                file_url = f"{repoLink}/blob/main/{link}"
                driver.get(file_url)
                raw_file_link = f"{repoLink}/raw/main/{link}"
                driver.get(raw_file_link)
                html = driver.page_source
                html = f"{html}"
                if "password" in html:
                    print(f"Password was found in {file_url}")
                time.sleep(1)

        open_file_and_search_password()


driver = webdriver.Chrome()
driver.get(str(github_page))
repos = driver.find_elements(By.CLASS_NAME, "repo")
repositories = driver.execute_script("""
    var contents = [];
    var elements = arguments[0];
    for (var i = 0; i < elements.length; i++) {
        contents.push(elements[i].textContent);
    }
    return contents
""", repos)

repositories_link = []
for repo in repositories:
    the_link = f"{github_page}/{repo}"
    repositories_link.append(the_link)

go_to_the_repo()

driver.quit()

