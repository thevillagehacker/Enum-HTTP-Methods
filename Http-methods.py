import requests
import sys
from requests.structures import CaseInsensitiveDict

headers=CaseInsensitiveDict()
print("""
	       __  __ ______ ______ ____                
	      / / / //_  __//_  __// __ \               
	     / /_/ /  / /    / /  / /_/ /               
	    / __  /  / /    / /  / ____/                
	   /_/ /_/  /_/    /_/  /_/                     
    __  ___       __   __                __     
   /  |/  /___   / /_ / /_   ____   ____/ /_____
  / /|_/ // _ \ / __// __ \ / __ \ / __  // ___/
 / /  / //  __// /_ / / / // /_/ // /_/ /(__  ) 
/_/  /_/ \___/ \__//_/ /_/ \____/ \__,_//____/ 

	          ------------------          
	       ~ |Do Hacks to Secure| ~
	          ------------------
	    https://twitter.com/thevillagehackr
	    https://github.com/thevillagehacker 

Usage: Python3 HTTP.py <URL>
""")
print("Warning: Please add authz token in the code to check the authorized endpoints")
url = sys.argv[1]

# add the authz token header below change the header name accordingly
headers["Authorization"] = ""

try:
	r = requests.get(url, headers=headers)
	print("\n[+] GET Request: ",r.status_code)
	r = requests.post(url, headers=headers)
	print("[+] POST Request: ",r.status_code)
	r = requests.options(url, headers=headers)
	print("[+] OPTIONS Request: ",r.status_code)
	print("[*] Allowed Headers:",r.headers["Allow"])
	r = requests.head(url, headers=headers)
	print("[+] HEAD Request: ",r.status_code)
	r = requests.put(url, headers=headers)
	print("[+] PUT Request: ",r.status_code)
	r = requests.patch(url, headers=headers)
	print("[+] PATCH Request: ",r.status_code)	
except requests.ConnectionError:
	print("Failed to connect")
