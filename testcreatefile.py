import os
try:
    if os.path.exists("demo.txt"):
        os.remove("demo.txt")
        f = open("demofile3.txt", "w")
        f.write("Woops, I have deleted the old file and content of this file")
        f.close()
    else:
        print("file does not exists")

finally:
        f = open("demofile3.txt", "r")
        print(f.read())
