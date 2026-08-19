#JSon datablob
data=[{"type":"programming","setup":"Why do programmers always get Christmas and Halloween mixed up?","punchline":"Because DEC 25 = OCT 31","id":382},{"type":"general","setup":"What do you get hanging from Apple trees?","punchline":"Sore arms.","id":228},{"type":"general","setup":"What do you call a troublesome Canadian high schooler?","punchline":"A poutine.","id":216},{"type":"general","setup":"What do you get when you cross a rabbit with a water hose?","punchline":"Hare spray.","id":231},{"type":"general","setup":"What’s 50 Cent’s name in Zimbabwe?","punchline":"200 Dollars.","id":149},{"type":"general","setup":"Why do pirates not know the alphabet?","punchline":"They always get stuck at \"C\".","id":349},{"type":"general","setup":"Why are fish so smart?","punchline":"Because they live in schools!","id":299},{"type":"general","setup":"Why are oranges the smartest fruit?","punchline":"Because they are made to concentrate. ","id":303},{"type":"general","setup":"If you boil a clown...","punchline":"Do you get a laughing stock?","id":44},{"type":"general","setup":"Did you know that protons have mass?","punchline":"I didn't even know they were catholic.","id":103}]
print()

#Identify All JSON data Keys and Values
print("1.All JSON data Keys and Values are:")
for joke in data:
    print()
    print("Joke")
    for key, value in joke.items():
        print(f"{key}: {value}")
print()

# Total Number of Keys in the JSON data
total_keys = len(data)
print(f"2.Total number of keys in the JSON data: {total_keys}")
print()

#Identify where the square brackets and curly braces are used in the JSON data
print("3.In a JSON data, the square brackets [] represent the list, \nand the curly braces {} represent each dictionary inside the list.")
print()

#Identify the data type of the JSON data
print("4.Identifying data type of the JSON data;")
print(type(data))
print("The JSON data type is a list of dictionaries")
print()

#Isolate one dictiionary from the JSON data
print("5.Isolated dictionary from the JSON data")
print()
print(data[0])



