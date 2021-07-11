import requests
from bs4 import BeautifulSoup
url = "https://peciis.info/PECMIS/Student/Hostel/StudentHostelPage.php"

r = requests.get(url)
collegecontent = r.content
# print(collegecontent)

soup = BeautifulSoup(collegecontent,'html.parser')
# print(soup.prettify)


anchor = soup.find_all('a')
print(anchor)