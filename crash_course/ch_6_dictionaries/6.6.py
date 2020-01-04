# Polling

favorite_languages = {
        'jen' : 'python',
        'sarah' : 'c',
        'edward' : 'ruby',
        'phil' : 'python'
        }

should_take_poll = ['jen', 'mike', 'steve', 'phil']

for name in should_take_poll:
    if name in favorite_languages:
        print( f"{name.title()}, Thanks for taking the poll!")
    else:
        print( f"{name.title()}, Please take the poll")

