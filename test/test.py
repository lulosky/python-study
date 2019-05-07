import time
from bs4 import BeautifulSoup
import urllib
import requests

# response = requests.get('https://en.wikipedia.org/wiki/Parrot')

# webHtml = response.text

# soup = BeautifulSoup(webHtml, "html.parser")

# print(soup.find_all('a'))
# EXAMPLE ------------------------------------------------------------------
# totalFood = ["tuna", "crispies", "shrimps", "lemon",  "glorious day"]

# sheLikes = True

# def boshka_likes(food_check):

#     global sheLikes

#     if food_check == "lemon":

#         print('boshka dont like lemon')
        
#         sheLikes = False


#     else:
#         sheLikes = True  

# while sheLikes:
#     food = totalFood.pop()


#     boshka_likes(food)

# print(totalFood)    
# END OF EXAMPLE ---------------------

# QUIZ continue_crawl FUNCTION ------------------------

article_chain = ['https://en.wikipedia.org/wiki/PICALM']

target_url = ['https://en.wikipedia.org/wiki/Family_(biology)']



def continue_crawl(search_history, target_url, max_steps=25):
        
        if search_history[-1] == target_url or len(search_history) > 25 or search_history[-1] in search_history[:-1]:
                return False
        else:
                return True
# # End QUIZ----------------------------


# # QUIZ Add a Link to the Article Chain ---------------------



def find_first_link(url):
        response_server = requests.get(url)
        html = response_server.text
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find(id='mw-content-text').find(class_="mw-parser-output")
        
        

        for i in div.find_all('p', recursive = False):
                if i.find('a', recursive = False):
                        url_path = i.find('a', recursive = False).get('href')
                      
                        break

        if not url_path:
                return
       
        


        full_link = urllib.parse.urljoin('https://en.wikipedia.org/', url_path)

        return full_link

while continue_crawl(article_chain, target_url): 
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        article_chain.append(first_link)
        # add the first link to article chain
        # delay for about two seconds
        print(article_chain[-1])
        time.sleep(2)


