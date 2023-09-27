import requests
import bs4

ind=0
selected_titles=[]
while ind<50:
    ind+=1
    base_url=f"https://books.toscrape.com/catalogue/page-{ind}.html"
    result=requests.get(base_url)
    soup=bs4.BeautifulSoup(result.text,"lxml")
    books=soup.select(".product_pod")
    for book in books:
        if 'star-rating Four' in str(book):
            book_title=book.select("a")[1]["title"]
            selected_titles.append(book_title)
selected_titles.sort()
print("This is a list of all of the books with a four star rating sorted by alphabetical order")
print("==============================================================================================")

for i,book in enumerate(selected_titles):
    print(f"{i+1}:{book}")