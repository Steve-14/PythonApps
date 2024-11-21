


playlist = {
    "LSD": {"artist": "The Beatles", "genre": "Pop"},
    "Blinding Lights": {"artist": "Beyonce", "genre": "Pop"},
    "Sandman": {"artist": "Metallica", "genre": "Metal"},
    "Buffalo Soldier": {"artist": "Bob Marley", "genre": "Reggae"},
    "Awful Shriek": {"artist": "Adele", "genre": "Soul"}
    }

artists_genres = {
    "The Beatles": "Rock",
    "Beyoncé": "Pop",
    "Miles Davis": "Jazz",
    "Taylor Swift": "Country",
    "Kendrick Lamar": "Hip-Hop",
    "Adele": "Soul",
    "Metallica": "Metal",
    "Bob Marley": "Reggae",
    "Daft Punk": "Electronic",
    "Elton John": "Pop/Rock",
}

#print(playlist)

"""Write a function called ‘add_song’ that takes three parameters: ‘title’, ‘artist’, 
        and ‘genre’. This function should add a new song to the playlist dictionary."""

#def add_song(title,artist,genre):
    #playlist.update({title:{"artist":artist,"genre":genre}})
    #print(f"The song{title} added to list")

#add_song("woosh","Rush","Rock")


"""Write a function called ‘view_playlist’ that prints out all the songs in the playlist 
in a readable format."""

#def view_playlist():    
        #print("Curent Songs are:")
        #for items in playlist:
            #print(items)
        
#view_playlist()

"""Write a function called ‘update_song’ that allows you to update the artist or 
    genre of a specific song. This function should take the title of the song to be 
    updated and the new artist or genre as parameters."""

#def update_song(artist,genre):
     #song = input("Please enter name of song to correct")
     #playlist.update({song:{"artist":artist,"genre":genre}})
     
##update_song()

#print(playlist)

"""Write a function called ‘delete_song’ that takes a song title as a parameter and 
    removes that song from the playlist."""

    
def delete_song():
    song = input("Please enter name of song to delete: ")
    del playlist[song]

delete_song()

print(playlist)