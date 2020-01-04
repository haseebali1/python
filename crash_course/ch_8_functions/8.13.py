# User Profile

# ** makes a dictionary of an arbitrary number of key-value pairs
def build_profile(first , last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('jack', 'daniels', location='apples',
        field='comp sci', birthday='12/3/13' )

print (user_profile)

for key, value in user_profile.items():
    print (key + " : " + value.title() )
