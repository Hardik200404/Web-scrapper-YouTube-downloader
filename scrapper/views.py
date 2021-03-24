from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def scrapper(website_url):
    source=requests.get(website_url).text
    s=BeautifulSoup(source,'html5lib')#parsing the given url
    my_dict=dict()
    for i in s.find_all('article'):
        h=i.h2.a.text
        try:
            vid_s=i.find('iframe',class_='youtube-player')['src']
            vid_id=vid_s.split("/")[4]
            vid_id=vid_id.split("?")[0]                        
        except Exception as err:
            vid_s="no link"
     
        yt_link=f"https://youtube.com/watch?v={vid_id}"
        my_dict[h]=yt_link
    return(my_dict)
        
def home(req):
    if req.method=='POST':
        website_url=req.POST['site-url']
        links=scrapper(website_url)
        context={
            'data':links
        }
        return render(req,'scrapper_templates/result.html',context)

    return render(req,'scrapper_templates/home.html')
