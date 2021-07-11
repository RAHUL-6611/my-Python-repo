import os

def mainfunction():
    print("this is for you")
    
def onlyforthisfile():
    print("isko sirf me use kar sakta hu")

if (__name__ == "__main__"):                         # other files cannot use this
    print(os.listdir("/"))
    print("Rahul is mahadev's bhakt")
    onlyforthisfile()    