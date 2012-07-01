import urllib
import urlparse
import httplib
import sys

def bawandar(url):
	response = urllib.urlopen(url)
	if response.getcode() == 200:
		#do all other things
		final_url = response.url
		print("final url: "+final_url)
		url_obj = urlparse.urlparse(final_url)
		conn = httplib.HTTPConnection(url_obj.netloc)
		conn.request("HEAD",url_obj.path)
		res = conn.getresponse()
		header_list = res.getheaders()
		#converting this header_list into a dictionary
		header_dict={}
		for x,y in header_list:
			header_dict[x]=y
		print("Content type: "+header_dict['content-type'])
		return {"data":header_dict,"flag":1} 		
	else:
		print("Failed to reach to the url")
		return {"data":None,"flag":0}
	

if __name__ == '__main__':
	url = sys.argv[1]
	a=bawandar(url)
	if a.flag==1:
		print(a.data['content-type'])
