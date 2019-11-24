# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:55:20 2019

@author: Asus
"""

# pyaudio em phải tải và cài từ https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

import pyaudio
import wave

print("Mời thầy nhập tên tệp âm thanh")
filename = input()

# Set chunk size of 92160 samples per data frame
chunk = 92160

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunksF
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data += wf.readframes(chunk)   # Tạo lặp lại vô hạn
    

# Close and terminate the stream
stream.close()
p.terminate()
