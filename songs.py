import mysql.connector
songs = []


db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="musicplayer"
        )

#create a cursor
mycursor = db.cursor()

def get_total_number_of_songs():
    #execute an sql query
    mycursor.execute("SELECT COUNT(*) FROM songs;")
    return mycursor.fetchall()[0][0]
    
def get_song_id():
    #execute an sql query
    mycursor.execute("SELECT id FROM songs;")

    #fetch all rows
    result = mycursor.fetchall()

    return result

def get_song_name( ):
    #execute an sql query
    mycursor.execute("SELECT name FROM songs;")

    #fetch all rows
    result = mycursor.fetchall()

    return result

def get_song_artist( ):
    #execute an sql query
    mycursor.execute("SELECT artist FROM songs;")

    #fetch all rows
    result = mycursor.fetchall()

    return result

def get_song_album( ):
    #execute an sql query
    mycursor.execute("SELECT album FROM songs;")

    #fetch all rows
    result = mycursor.fetchall()

    return result

def get_song_genre( ):
    #execute an sql query
    mycursor.execute("SELECT genre FROM songs;")

    #fetch all rows
    result = mycursor.fetchall()

    return result

def get_song_location( ):
    #execute an sql query
    mycursor.execute("SELECT location FROM songs;")

    #fetch all rows
    result = mycursor.fetchall()

    return result


def get_songs():
    for i in range(0, int(get_total_number_of_songs())):
        ids = get_song_id()
        names = get_song_name()
        genre = get_song_genre()
        artist = get_song_artist()
        album = get_song_album()
        location = get_song_location()
        songs.append(
            {
                'id': ids[i][0],
                'name': names[i][0],
                'genre': genre[i][0],
                'artist':artist[i][0],
                'album':album[i][0],
                'location':location[i][0]
            }
        )

    return songs

def get_specific_songs(genre):
    out=[]
    for song in songs:
            if song['genre'] == genre:
                out.append(song)

def get_genre_specific_songs(index):
    out=[]
    if index == 1:
        out.append(get_specific_songs('rhymes'))
        
    elif index == 2:
        out.append(get_specific_songs('pop'))
    elif index == 3:
        out.append(get_specific_songs('hiphop'))
        out.append(get_specific_songs('pop'))
    elif index == 4:
        out.append(get_specific_songs('rock'))
    elif index ==5:
        out.append(get_specific_songs('bhajans'))


    return out

print(get_song_name())