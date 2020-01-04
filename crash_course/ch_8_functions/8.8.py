# User Album

def make_album(artist, album_title, number_songs=None):
    if number_songs:
        album = { 'artist' : artist, 'title': album_title, 'songs': \
                number_songs }
    else:
        album = { 'artist' : artist, 'title': album_title }
    return album

artist = ""
album_title = ""

while artist != 'quit' or album_title != 'quit':
    print ("\nEnter the album information. Enter quit to exit anytime:")
    artist =  input("Enter the artist : ")
    album_title =  input("Enter the album : ")

    if artist == 'quit' or album_title == 'quit':
        break
    else:
        print(make_album(artist, album_title))

