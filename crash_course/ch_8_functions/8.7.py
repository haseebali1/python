# Album

def make_album(artist, album_title, number_songs=None):
    if number_songs:
        album = { 'artist' : artist, 'title': album_title, 'songs': \
                number_songs }
    else:
        album = { 'artist' : artist, 'title': album_title }
    return album

print (make_album("sd dsf", "afd sdfal adflsa"))
print (make_album("kjfldsaf djlakw", "eirwp weriuw wriuwe weriuw", 7))
print (make_album("jafsl ajskldf", "cnz,m nxnvmx nbksdfi"))
