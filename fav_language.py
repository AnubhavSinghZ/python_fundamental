fav_lang={
    "anu": "Python",
    "prin": "Python",
    "aman": "html",
    "abhi": "c++",
}


friends=["abhi", "prince"]
for name in fav_lang.keys():
    print(f"Hi {name}")
    if name in friends:
        languages=fav_lang[name].title()
        print(f"\t{name.title()}, I see you love C")
    if "erin" not in fav_lang:
        print("Erin, please take our poll")
for name in sorted(fav_lang.keys()): #this will sort the name 
    print(f"{name.title()}, thank you for taking the poll")

#code correction