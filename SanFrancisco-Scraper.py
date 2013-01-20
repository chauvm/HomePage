from bs4 import BeautifulSoup

voyage_cities = ["C:\Users\Chau Vu\Downloads\New York City.htm",
                  "C:\Users\Chau Vu\Downloads\San Francisco.htm",
                  "C:\Users\Chau Vu\Downloads\San Jose.htm"]

wiki_cities = ["C:\Users\Chau Vu\Downloads\New York City - Wikipedia, the free encyclopedia.htm",
               "C:\Users\Chau Vu\Downloads\San Francisco - Wikipedia, the free encyclopedia.htm",
               "C:\Users\Chau Vu\Downloads\San Jose, California - Wikipedia, the free encyclopedia.htm"]

for i in range(len(voyage_cities)):
    soup = BeautifulSoup(open(voyage_cities[i]))
    soupGeo = BeautifulSoup(open(wiki_cities[i]))
    title= (soup.find(id="firstHeading").find("span").get_text())   #get TITLE
    print title

    img = soup.find(id="mw-content-text").find("div").find("div").find("a").get('href')
    print img           #get IMG

    latitude = soupGeo.find("span", {"class":"latitude"}).get_text()
    longitude = soupGeo.find("span", {"class":"longitude"}).get_text()

    print latitude, longitude        #lat and long of destination

    first_paragraph = soup.find(id="mw-content-text").find("p").get_text()
    print first_paragraph    # first paragraph

    print "\n"
