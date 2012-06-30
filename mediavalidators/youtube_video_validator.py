import urlparse
import httplib
import sys

def validate_video(key):
	url='http://gdata.youtube.com/feeds/api/videos/'+key
	url_obj = urlparse.urlparse(url)
	conn=httplib.HTTPConnection(url_obj.netloc)
	conn.request("HEAD",url_obj.path)
	response=conn.getresponse()
	if response.status == 200:
		print("Youtube video is valid")
		return 1
	if response.status == 404:
		print("Sorry!the video doesn't seem to be valid")
		return 0

if __name__ == '__main__':
	key = sys.argv[1]
	validate=validate_video(key)
