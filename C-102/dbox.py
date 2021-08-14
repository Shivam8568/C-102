import cv2 
import dropbox
import time 
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        trdult = False
    return img_name 
    print ("Snapshot taken") 
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    accesstoken = "gCbOD0wOJKcAAAAAAAAAAUG-yzXt6vGs3PuxhiYT0f6WCOS0VmaBl7tCwpd6SVEh"
    file = img_name
    file_from = file 
    file_to = "/testfolder/"+ (img_name)
    dbx = dropbox.Dropbox(accesstoken)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()- start_time)>=5):
            name = take_snapshot()
            upload_file(name)
main()