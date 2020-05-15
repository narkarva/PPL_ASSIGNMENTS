try:
    f1 = open(input('Enter filename to ne opened\n'), mode = input('Enter mode in which file is to be opened\n'))
    print(f1.read())
    f1.write('This is the new line i am trying to add in the file')
except(UnicodeDecodeError):
    print("Error!   Please check that file to be opened is readable")
except(FileNotFoundError):
    print("Error! Please check that filename and path is correct")
except(IsADirectoryError):
    print("Error! Can't open a directory")
except(PermissionError):
    print("Error! Please check the permissions of file to be opened")
except:
    print("Error! Something went wrong")
finally:
    print("This is printed irrespective of exception has occured or not")

