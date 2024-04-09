name = "Philip"
print(name)

def say_hello():
    print("Hello Friend")
    print("I'm inside the funtion")

say_hello()


# data structures
# array js -> list python
prices = [2, 4, 5, 6, 23]

# add to list
prices.append(999)
print(prices)

# sum all the prices
total = 0
for price in prices:
    total += price

print(total)

# dictionary
philip = {
    "age": 31,
    "handsome": True,
    "height": "8ft 14in",
    "marital_status": "Not In-Love",
    "special_move": "deep sleep",
    "hobbies": [],
    "address": {
        "planet": "urth",
        "continent": "north amerikuh"
    }
}

print(philip)

# read from  dictionary
# print(philip["handsome"])
# print(philip["address"])


# modify dictionary
philip["age"] = 99


# add keys to dictionary
philip["is_hungry"] = True

print(philip)


