import requests
from bs4 import BeautifulSoup as bs

# Github web scraper
# github_user = input('Input Github User: ')
# url = 'https://github.com/' + github_user
# r = requests.get(url)
# soup = bs(r.content, 'html.parser')
# profile_image = soup.find('img', {'alt': 'Avatar'})['src']
# print(profile_image)

insta_user = input('Input Instagram User: ')
url = 'https://instagram.com/' + insta_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('profile_pic_url') + 21
print(profile_image)
