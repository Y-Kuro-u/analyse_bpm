import sys
import os
import pydub as dub
from pydub.playback import play
import shutil
import tempfile as temp
import librosa

class TransToWav():

    def __init__(self,dir_path,_path):
        self.path = os.path.join(dir_path,_path)
        self.split_path = os.path.splitext(self.path)
        self.ext = self.split_path[-1]
        self.file_name = _path
        self.save_file = tmp.name +"/"+ self.file_name + ".wav"

    def trans_wav(self):
        self.music = dub.AudioSegment.from_mp3(self.path)
        self.music.export(self.save_file,format="wav")

    def save_wav(self):
            if self.ext == ".mp3":
                self.trans_wav()
            elif self.ext == ".wav":
                shutil.copyfile(self.path,self.save_file)
            else:
                pass

class WavSaveTmp():

    def __init__(self,path):
        self.path = path
        if os.path.isdir(self.path) is True:
            self.dir_path = self.path
            self.file_name = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,f))]
        elif os.path.isfile(path) is True:
            self.dir_path = os.path.dirname(self.path)
            self.file_name = os.path.basename(self.path)
        else:
            pass
        
    
    def save_tmp(self):
        if type(self.file_name) is list:
            for i in self.file_name:
                handle_wav = TransToWav(self.path,i)
                handle_wav.save_wav()
        else:
            handle_wav = TransToWav(self.dir_path,self.file_name)
            handle_wav.save_wav()

class play_music():

    def __init__(self):
        self.wav_name = os.listdir(tmp.name)
        self.path = [tmp.name + "/" + i for i in self.wav_name]

    def play(self):
        for i in self.path:
            self.sound = dub.AudioSegment.from_wav(i)
            print(type(self.sound))
            play(self.sound)
        self.play()


class BpmAnalyse():
    def __init__(self):
        self.dir_path = tmp.name
        self.file_names = os.listdir(self.dir_path)
        self.file_path = [self.dir_path + "/" + i for i in self.file_names]
        self.bpm = {}

    def analyse_bpm(self):
        for file_name,path in zip(self.file_names,self.file_path):
            if file_name not in self.bpm:
                self.music, self.sr = librosa.load(path)
                self._bpm =  librosa.beat.tempo(self.music,self.sr)
                self.bpm[file_name] = int(self._bpm[0])
            else:
                continue    
        return self.bpm

#path
path = sys.argv[1]
#make temp directory
tmp = temp.TemporaryDirectory()

#mp3,wav save to temp file
save_ = WavSaveTmp(path)
save_.save_tmp()

#play music in temp directory (loop)
"""
music = play_music()
music.play()
"""

#bpm analyse
analyser = BpmAnalyse()
bpm_list = analyser.analyse_bpm()

#clean up temp directory
tmp.cleanup()

