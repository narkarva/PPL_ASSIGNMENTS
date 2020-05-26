import os
import shutil
import speech_recognition as sr
from gtts import gTTS

def speechtotext() :
    r = sr.Recognizer()
    mic = sr.Microphone(device_index = 0,chunk_size = 20000,sample_rate = 48000)
    with mic as source :
        r.adjust_for_ambient_noise(source)
        aud = r.listen(source)
    p = r.recognize_google(aud)
    return p

def introspeech() :    
    intro = "What can I do for you with files and folders?"
    tts1 = gTTS(intro,lang = 'en')
    tts1.save('intro.mp3')
    os.system('mpg123 intro.mp3')

def current_directory() :
    print(os.getcwd())

def contents_here() :
    print(os.listdir())

def create_new() :
    name_new = "What should be name of new directory?"
    tts2 = gTTS(name_new,lang = 'en')
    tts2.save('name_new.mp3')
    os.system('mpg123 name_new.mp3')
    name = speechtotext()
    print(name)
    os.mkdir(name)

def change_directory() :
    name_dir = "Please name directory you want to change to."
    tts2 = gTTS(name_dir,lang = 'en')
    tts2.save('name_dir.mp3')
    os.system('mpg123 name_dir.mp3')
    name = speechtotext()
    name = name.title()
    print(name)
    if(name == 'Desktop') :
        os.chdir('/home/ubuntu/Desktop')
    elif(name == 'Downloads') :
        os.chdir('/home/ubuntu/Downloads')
    elif(name == 'Documents') :
        os.chdir('/home/ubuntu/Documents')
    elif(name == 'Music') :
        os.chdir('/home/ubuntu/Music')
    elif(name == 'Videos') :
        os.chdir('/home/ubuntu/Videos')
    elif(name == 'Pictures') :
        os.chdir('/home/ubuntu/Pictures')
    else :
        print("No such directory found\n")

def rename_file() :
    name1_file = "Please name file you want to rename"
    tts2 = gTTS(name1_file,lang = 'en')
    tts2.save('name1_file.mp3')
    os.system('mpg123 name1_file.mp3')
    name1 = speechtotext()
    print(name1)
    name2_file = "What should be the new name of file?"
    tts2 = gTTS(name2_file,lang = 'en')
    tts2.save('name2_file.mp3')
    os.system('mpg123 name2_file.mp3')
    name2 = speechtotext()
    print(name2)
    print("Select file extension :\n 1. .c\n 2. .txt\n 3. .mp3\n")
    while 1 :
        k = int(input("Make your choice"))
        if (k == 1) :
            ext = ".c"
            break
        elif (k==2) :
            ext = ".txt"
            break
        elif (k == 3) :
            ext = ".mp3"
            break
        else :
            print("No match found, enter another choice.\n")
    name1 = name1+ext
    name2 = name2+ext
    print(name1)
    print(name2)
    try :
        os.rename(name1,name2)
        print("File renamed successfully! \n")
    except :
        print("Something went wrong, try again\n")

if __name__ == "__main__" :
    
    while 1:
        introspeech()
        p = speechtotext()
        print(p)
        if (p == "show") :
            current_directory()
        elif (p == "contents") :
            contents_here()
        elif (p == "create") :
            create_new()
        elif(p == "change") :
            change_directory()
        elif (p == "rename") :
            rename_file()
        elif (p == "close") :
            break
        else :
            print("Didnt get what you are trying to say\n")
