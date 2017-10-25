import urllib.request
from bs4 import BeautifulSoup

class DataScrapper:

    def get_results(self,url):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent':user_agent,}
        request = urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        return response

    def get_twitter_results(self):
        url = "https://twitter.com/search?q=reactjs"
        response = self.get_results(url)
        data = BeautifulSoup(response.read(),'lxml')
        all_tweets = data.findAll("div", { "class" : "dir-ltr" })[0]
        return all_tweets

    def get_google_results(self):
        url = "https://www.google.co.in/search?q=reactjs"
        response = self.get_results(url)
        data = BeautifulSoup(response.read(),'lxml')
        all_results = data.findAll("cite")
        return all_results
        