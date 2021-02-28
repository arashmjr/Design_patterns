from typing import List
from SongModel import SongModel


class SoundManager:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if SoundManager.__instance == None:
            SoundManager()
        return SoundManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SoundManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SoundManager.__instance = self


    def play_songs(self, songs: List[(SongModel)], index: int):
        self.current_song = songs[index]
        self.isPlaying = True
        print("song is play")
        print(self)

    def next_song(self, songs:List[(SongModel)], index: int):
        self.current_song = songs[index + 1]
        self.isPlaying = True
        print(self)

    def previous_song(self, songs:List[(SongModel)], index: int):
        self.current_song = songs[index - 1]
        self.isPlaying = True
        print(self)

    def pause_song(self, songs: List[(SongModel)], index: int):
        self.current_song = songs[index]
        self.isPlaying = False
        print(self)

    def resume_song(self, songs: List[(SongModel)], index: int):
        self.current_song = songs[index]
        self.isPlaying = True
        print(self)












# status = {'initial', 'playing', 'paused'}

# def set_song(self, new_song):
#     status['initial'] = new_song
#     print("song is set")

#
# def play(self):
#     global status
#     print("song is playing")
#     return status[1]
#
# def pause(self):
#     global status
#     print("song is paused")
#     return status[2]



