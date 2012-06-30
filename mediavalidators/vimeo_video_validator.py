import urllib
import sys
from BeautifulSoup import BeautifulStoneSoup

def validate_video(key,type):
        url='http://vimeo.com/api/v2/video/'+key+"."+type
	usock=urllib.urlopen(url)
        #print(usock.read())
        if usock.getcode() == 200:
		print("Vimeo video is valid")
		soup = BeautifulStoneSoup(usock.read())
		#print(soup.prettify())
	if usock.getcode() == 404:
		print("Sorry!Vimeo video doesn't seem to be valid")

if __name__ == "__main__":
	key=sys.argv[1]
	type=sys.argv[2]
	validate=validate_video(key,type)
