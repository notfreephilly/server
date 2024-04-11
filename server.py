from flask import Flask, request
import json
from config import dev, sum
from data import catalog
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #disables CORS policy

@app.get("/") # decorator
def hello():
    return "Hello from Phils Flask"

@app.get("/test")
def test():
    return "Test page!!"

@app.get("/about")
def about():
    return "About: Philip, The Mysterious"





# #################################
####### API METHODS ############
###################################




@app.get('/api/developer')
def developer():
    return json.dumps(dev)

@app.get('/api/sum')
def simple_sum():
    ans = sum(21,43)
    return json.dumps(ans)

@app.get('/api/products')
def get_catalog():
    return json.dumps(catalog)


@app.post("/api/products")
def save_product():
    prod = request.get_json() #read the payload of request
    catalog.append(prod)

    return json.dumps(prod)



# start the server
app.run(debug=True)
