# Book-Price-Web-Scraper
Web scraper utilizes HTTP requests to receive a book name and returns a price as a string.
<br> 
<br>  

## Requesting Data
1) To REQUEST data from the web scraper, an HTTP request must be made to the url that the project is hosted on. 
2) Locally, the URL will be 'http//127.0.0.1:5000/price'. '/price' is also added to it for routing purposes.
4) When making a HTTP request, be sure to include the parameters as {'name': 'name of book'}.
5) The URL will then show as 'http//127.0.0.1:5000/price/name+of+book', which is the correct routing.
6) Server-wise, the procedure is the same, but the url will change. ex. 'http//randomserver/price/name+of+book'.

**Example:**  
(Python) <br>  
import requests  
r = requests.get('http//127.0.0.1:5000/price', params = {'name': 'name of book'})
<br>  
<br>  

## Receiving Data
1) The data received should be in the variable you stored the requests.get in. (in above example, this is 'r')
2) Use r.text to access it.
<br>  
<br>  

## For further help, please view testing.py
Note: time.sleep() is added so that spamming requests will not break the connection.
<br>  
<br>  


## UML Sequence Diagram

![image](https://user-images.githubusercontent.com/89036725/236707407-8ad67597-2df8-4a8e-9599-8aebec9118d3.png)
