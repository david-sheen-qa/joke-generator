# import the Flask class
from flask import Flask

# import the Requests module
import requests

# create an instance of the Flask class
app = Flask(__name__)

# use the route() decorator to tell Flask what URL should trigger our function
@app.route('/', methods=['GET'])
def display_joke():
    url1 = "https://api.namefake.com"
    url2 = "https://api.icndb.com/jokes/random"

    # make a request to url1
    r1 = requests.get(url1)
    # returns a JSON object of the result
    response1 = r1.json()
    # parse the JSON object for 'name' and capture it
    full_name = response1['name']
    #split the string on whitespace from the end
    first_name = full_name.rsplit(' ', 1)[0]
    last_name = full_name.rsplit(' ', 1)[1]
    #set the payload for the next request
    payload = {'firstName': first_name, 'lastName': last_name}

    # make a request to url2, and pass payload 
    r2 = requests.get(url2, params=payload)
    # returns the JSON object of the result
    response2 = r2.json()
    # parse the JSON object for nested dictionary 'value' > 'joke' and return it 
    return response2['value']['joke']

app.run()
