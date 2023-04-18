
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.app import App
import songs
import time
import random
import os

Window.size = (400,600)
kv = Builder.load_file('main.kv')
_age = 0

sm = ScreenManager()
songs_list = songs.get_songs()
songs_to_display_list = []

class FirstScreen(Screen):

    

    def submit(self):
        self.age = int(self.ids.age_input.text)
        global _age 
        _age = _age + int(self.ids.age_input.text)
        print(_age)
        SecondScreen().a = int(self.ids.age_input.text)
        
        if self.age <10:
            for song in songs_list:
                if song['genre']=='0':
                    songs_to_display_list.append(song)
                    
        elif self.age <18:
            for song in songs_list:
                if song['genre']=='1':
                    songs_to_display_list.append(song)
        
        elif self.age <30:
            for song in songs_list:
                if song['genre']=='2':
                    songs_to_display_list.append(song)
                    
        elif self.age <60:
            for song in songs_list:
                if song['genre']=='3':
                    songs_to_display_list.append(song)
    
        elif self.age >60:
            for song in songs_list:
                if song['genre']=='4':
                    songs_to_display_list.append(song)


class SecondScreen(Screen):
        
        def on_enter(self):
            self.a = int(self.manager.get_screen("first").ids.age_input.text)
            self.music_directory=[]
            if len(self.music_directory) == 0:
                
                if self.a <10:
                    self.music_directory = 'music/'+'1'
                elif self.a <17:
                    self.music_directory = 'music/'+'2'
                elif self.a <39:
                    self.music_directory = 'music/'+'3'
                elif self.a <60:
                    self.music_directory = 'music/'+'4'
                elif self.a >60:
                    self.music_directory = 'music/'+'5'
                self.music_files = os.listdir(self.music_directory)
                self.song_files = [x for x in self.music_files if x.endswith('.mp3')]
                
                
                

        def play_audio(self):
            self.progressbar = self.ids.progress_bar
            self.play_button = self.ids.play
            self.stop_button = self.ids.stop
            self.album_image = self.ids.album_image
            self.current_time = self.ids.current_time
            self.total_time = self.ids.total_time
            self.song_label = self.ids.song_label


            self.song_count = len(self.song_files)
            self.image_files =  os.listdir('assets/background')
            self.sound = None            

            self.play_button.disabled = True
            self.stop_button.disabled = False
            self.song_title = self.song_files[random.randrange(0,self.song_count)]
            self.sound = SoundLoader.load('{}/{}'.format(self.music_directory, self.song_title))
            self.song_label.text = self.song_title
            self.album_image.source = 'assets/background/'+self.image_files[random.randrange(0,len(self.image_files))]
            print(self.image_files[random.randrange(0,len(self.image_files))])

            self.progressbarEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length/60)
            self.set_timeEvent = Clock.schedule_interval(self.set_time,0.5)

            self.sound.play()

        def update_progressbar(self, value):
            
            if self.progressbar.value <100:
                self.progressbar.value += 1

        def stop_audio(self):
            self.play_button.disabled = False
            self.stop_button.disabled = True
            self.sound.stop()
            self.progressbarEvent.cancel()
            self.set_timeEvent.cancel()
            self.progressbar.value = 0
            self.current_time.text = '00:00'
            self.total_time.text = '00:00'

        def set_time(self, t):
            current_time = time.strftime('%M:%S',time.gmtime(self.progressbar.value))
            total_time = time.strftime('%M:%S',time.gmtime(self.sound.length))

            self.current_time.text = current_time
            self.total_time.text = total_time

        def volume(self, *args):
            self.sound.volume = float(args[1])
    

class ThirdScreen(Screen):
    _songs = songs.get_songs()
    
    def on_enter(self):
        age = int(self.manager.get_screen("first").ids.age_input.text)
        self.manager.get_screen("first").ids.age_input.text = "0"
        a=0
        if age <10:
            a=1
        elif age<17:
            a = 2
        elif age<39:
            a= 3

        elif age<60:
            a = 4
        elif age>=60:
            a = 5
        
        if age>0:
            self.name_ly= self.ids.songs_name_list
            self.artist_ly= self.ids.songs_artist_list
            self.album_ly= self.ids.songs_album_list
            for i in self._songs:
                if int(i['genre'])==a:
                    self.name_ly.add_widget(Label(text = i['name']))
                    self.artist_ly.add_widget(Label(text = i['artist']))
                    self.album_ly.add_widget(Label(text = i['album']))



sm.add_widget(FirstScreen(name = 'first'))
sm.add_widget(SecondScreen(name = 'second'))
sm.add_widget(ThirdScreen(name = 'third'))

class RunApp(App):
    def build(self):
        return sm
    
if __name__ == '__main__':
    RunApp().run()
