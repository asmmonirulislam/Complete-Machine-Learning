d = {} #empty dictionary
print(type(d)) #<class 'dict'>


marks = {
    "sayem":100,
    "saiful":94,
    "sojib": 45
}

print(marks) #{'sayem': 100, 'saiful': 94, 'sojib': 45}
print(type(marks)) #<class 'dict'>
print(marks["sayem"]) #100
print(marks["sojib"]) #45

a = {
    "monirul":"code",
    "list":[1,2,3] 
}
print(a["monirul"]) #code
print(a["list"]) #[1, 2, 3]

for key, value in a.items():
    print(f"{key} -> {value}")
    
# Output: 
# monirul -> code
# list -> [1, 2, 3]

# -------------------------------------------------

# properties of python dictionaries:
# 1. it is unordered
# 2. it is mutable
# 3. it is indexed
# 4. cannot contain duplicate keys

# DICTIONARY METHODS

dict = {
    "sayem": 100,
    "hafiza": 99,
    0: "monirul"
}

# 01. items() - returns a list of key tuples
print(dict.items()) #dict_items([('sayem', 100), ('hafiza', 99), (0, 'monirul')])
# 02. keys() - returns a list containing dictionary's keys
print(dict.keys()) #dict_keys(['sayem', 'hafiza', 0])
# 03. update({"friends":}) - updates the dictionary with supplied key value pairs
dict.update({"hafiza":98, "saiful":80})
print(dict) #{'sayem': 100, 'hafiza': 98, 0: 'monirul', 'saiful': 80}
# 04. get("name") - returns the value of the specified keys (and the value is returned)
print(dict.get("monirul")) #None
print(dict.get("sayem")) #100
# 05. clear() - wipes the dictionary
marks.clear()
print(marks) #{}
# 06. member checking
print("sayem" in dict) #True
# 07. len() - size of the dictionary
print(len(dict)) #4
# 08. pop(x) - removes x from the dictionary
val = dict.pop("saiful")
print(val) #80
print(dict) #{'sayem': 100, 'hafiza': 98, 0: 'monirul'}