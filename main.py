__author__ = "dhruvmullick"

from bs4 import BeautifulSoup
import urllib2

more = ""

while more!='n':
    url2 = str(raw_input("Enter the user's SPOJ id: "))
    url = "http://www.spoj.com/status/"+url2+"/"
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)


    count = 0

    for link in soup.find_all("table", attrs={"class" : "problems"}):       #in the problem table looks at all the rows and displays the title if it is a problem

        for link2 in link.find_all("tr"):

            if(count>10):
                break
            count = count+1
            for linkDate in link2.find_all("td",attrs={'class': 'status_sm'}):
                print linkDate.get_text(),
            for link3 in link2.find_all("a"):
                theName = link3.get('title')
                if theName!="See the best solutions":
                    print theName + " ",
                    print link3.get_text()
    more = str(raw_input("Do you want to stalk more? (y/n):"))


print "Hola"