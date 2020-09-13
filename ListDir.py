import os

CurDir = os.listdir("/home/nmeece/Desktop/projects/WorkRelated")
ScnDir = os.scandir("/home/nmeece/Desktop/projects/WorkRelated")


with ScnDir as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)