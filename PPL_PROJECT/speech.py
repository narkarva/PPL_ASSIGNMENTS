import speech_recognition as sr
import webbrowser as web
 
 
 
def main():

 
    url1="http://www.python.org"
    url2='https://www.google.com/'
    url3='https://www.wikipedia.org/'
    url4='https://www.geeksforgeeks.org/'
    url5='https://www.hackerrank.com/'
    url6='https://www.edx.org/'
    url7='https://www.coep.org.in/'

    a={'Google':url2,'python':url1,'Wikipedia':url3,'geek':url4,'hackerrank':url5,'edX':url6,'coep':url7}

    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something ")
 
        audio = r.listen(source)
 
        print("Recognizing Now ... ")
 
 
 
        try:
            dest = r.recognize_google(audio)
            print("You have said : " + dest)
            
            if dest == 'Google':
                web.open_new(a['Google'])
            elif dest == 'python':
                web.open_new(a['python'])
            elif dest == 'Wikipedia':
                web.open_new(a['Wikipedia'])
            elif dest == 'geek':
               web.open_new(a['geek'])
            elif dest == 'hackerrank':
                web.open_new(a['hackerrank'])
            elif dest == 'edX':
                web.open_new(a['edX'])
            elif dest == 'coep':
                web.open_new(a['coep'])
            elif dest =='close':
                print("You said close")
            elif dest!='python' and dest!='Wikipedia' and dest!='Google' and dest!='geek' and dest!='hackerrank' and dest!='edX' and dest!='coep' and dest!='close':
                web.open_new('https://moodle.coep.org.in/moodle/')
    
        except Exception as e:
            print("Error : " + str(e))
 
 
if __name__ == "__main__" :
    main()


