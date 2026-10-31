# This example contains Dictionary in Dictionary



users={

    'einstein':{
        'first': "Albert",
        'last': "Einstein",
        'Location': "princeton",
    },
    'mcurie':{
        'first': "marie",
        'last': "curie",
        'Location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\n Username:{username}")
    full_name= f"{user_info['first']} {user_info['last']}"
    location=user_info['Location']

    print(f"\tFull Name :{full_name.title()}")
    print(f"\tLocation: {location.title()}")
