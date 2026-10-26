prompt="if you share your name, we can personalize the mesg you see"
prompt+="\nwhat is your name?"

name =input(prompt)
print(f"\nHello {prompt}!")




height = int(input("How tall are you?")) # Asking to users that what's their height

if height >=48:
    print("YOu are tall enough to ride")
else:
    print("You are not too tall to ride")