import requests
import json
  
response = requests.get("https://zenquotes.io/api/random")
json_data = json.loads(response.text)

# This is how you will receive the json load: 
# [ {"q":"To be great is to be misunderstood.","a":"Ralph Waldo Emerson","h":"<blockquote>&ldquo;To be great is to be misunderstood.&rdquo; &mdash; <footer>Ralph Waldo Emerson</footer></blockquote>"} ]

#Separate the json load to "Quote" - Author format
quote = json_data[0]["q"] + " -" + json_data[0]["a"]
return quote