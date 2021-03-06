from SoundManager import SoundManager
from SongModel import SongModel


# song = SongModel(id= 52,
#                  name =  "ye mosht sarbaz",
#                  artist = "hichkas",
#                  genre = "Rap",
#                  duration = 150.5,
#                  url = "https://www.youtube.com/watch?v=4qw3qTV4608")

songs_list = [SongModel(id= 50,
                 name =  "ye mosht sarbaz",
                 artist = "hichkas",
                 genre = "Rap",
                 duration = 150.5,
                 url = "https://www.youtube.com/watch?v=4qw3qTV4608"),
SongModel(id= 51,
                 name =  "ye mosht sarbaz",
                 artist = "ho3ein",
                 genre = "Rap",
                 duration = 150.5,
                 url = "https://www.youtube.com/watch?v=4qw3qTV4608"),
SongModel(id= 52,
                 name =  "ye mosht sarbaz",
                 artist = "sadegh",
                 genre = "Rap",
                 duration = 150.5,
                 url = "https://www.youtube.com/watch?v=4qw3qTV4608")
              ]

SoundManager.get_instance().play_songs(songs_list, 1)
SoundManager.get_instance().next_song()
SoundManager.get_instance().previous_song()
SoundManager.get_instance().pause_song()

















