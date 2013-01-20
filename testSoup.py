from bs4 import BeautifulSoup
import urllib2, sys

hdr = {'User-Agent': 'Mozilla/5.0'}



voyage_cities = ["http://en.wikivoyage.org/wiki/San_Jose_(California)",
                 "http://en.wikivoyage.org/wiki/New_York_City"
                ]

wiki_cities = ["http://en.wikipedia.org/wiki/San_Jose_(California)",
               "http://en.wikipedia.org/wiki/New_York_City"
               ]
for i in range(len(voyage_cities)):
##    soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(voyage_cities[i], headers=hdr)))
##    soupGeo = BeautifulSoup(urllib2.urlopen(urllib2.Request(wiki_cities[i], headers=hdr)))
##    title= (soup.find(id="firstHeading").find("span").get_text())   #get TITLE
##    print title
##
##    img = soup.find(id="mw-content-text").find("div").find("div").find("a").get('href')
##    print "en.wikivoyage.org" + img           #get IMG
##
##    latitude = soupGeo.find("span", {"class":"latitude"}).get_text()
##    longitude = soupGeo.find("span", {"class":"longitude"}).get_text()
##
##    print latitude, longitude        #lat and long of destination
##
##    first_paragraph = soup.find(id="mw-content-text").find("p").get_text()
##    print first_paragraph    # first paragraph

    see = soup.

    print "\n"
