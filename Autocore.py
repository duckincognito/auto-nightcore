#!/usr/bin/env python3

print('\n Running... \n')

import sys
import pip


# Creates a function to install packages
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Takes in file name      
try:
    file_name = str(sys.argv[1])
except:
    file_name = input('What is the file name: \n')    

# Uses user specified keyword
try:
    keyword = str(sys.argv[2])
except:
    keyword = input('What keyword do you want: \n')  
 
keyword = 'Anime ' + keyword
   
# Checks if user specified how much to speed up the song, if not uses 1.2
try:
    increase = float(sys.argv[3])
except:
    increase = 1.2    
     
#Imports pydub and google image downloader
try:  
    from pydub import AudioSegment
except:
    install('pydub')
    from pydub import AudioSegment
    
try:
    from google_images_download import google_images_download
except:
    install('google_images_download')
    from google_images_download import google_images_download

try:
    import moviepy.editor as mpy
except:
    install('moviepy')
    import moviepy.editor as mpy

# Defines function to import audio files
def import_audio(soundFile):
    sound_type = file_name[-4:]
    if sound_type == '.mp3':
        sound = AudioSegment.from_mp3(soundFile)
    elif sound_type == '.wav': 
        sound = AudioSegment.from_wav(soundFile)
    return sound, sound_type

# Imports audio file
try:
    sound, sound_type = import_audio(file_name)
except:
    print('%s not found or is not an mp3 or wav file' % file_name)
    quit

# Changes the sample rate to change the song speed
new_sample_rate = int(sound.frame_rate * increase)
sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# Saved the sped-up song
nightcore_file = 'Nightcore_' + file_name
sound.export(nightcore_file)

# Uses keyword to find images on google
response = google_images_download.googleimagesdownload()
arguments = {"keywords":keyword,"limit":1,"print_urls":True,"format":"jpg", "size":">1024*768", "aspect_ratio":"wide", "output_directory":"Pics"} 
image_paths = response.download(arguments)

if type(image_paths) == tuple:
    image_paths = image_paths[0]
print('Image for video in' + image_paths[keyword][0])


# Gets Audio Length
duration = sound.__len__()



clip = mpy.ImageClip(image_paths[keyword][0])
clip.fps=60
clip = clip.set_duration(duration/1000)

clip.write_videofile(nightcore_file.split('.')[0] + '.mp4', audio=nightcore_file)

















