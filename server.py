from flask import Flask
import json
from config import dev, sum

app = Flask(__name__)


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





# start the server
app.run(debug=True)
