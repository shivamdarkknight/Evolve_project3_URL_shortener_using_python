#URL shortner through python by Shivam Tiwari
import requests

api_key = "c50fe58a6116beb956e66847ad3347dc82792"
# the URL you want to shorten
url = "https://www.youtube.com/watch?v=xd8dKY6Ozrg&t=3s" #Copying any URL from web
# preferred name in the URL
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
# or
# api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
# make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #After Generating url from running code
    #Pasting this generated url on web to check whether it works or not
    #Generated url :
    