import os
import shutil
import time

curDir = os.getcwd()
listDirectory = os.listdir()




for item in listDirectory:

    path = curDir + '\\' + item
    ext = os.path.splitext(item)

    if os.path.exists(path) == True:
        Time = time.time()
        cTime = os.stat(path).st_ctime


        date = Time
        cDate = cTime

        days30 = 60 * 60 * 24 * 30

        if date - cDate > days30:

            if ext[1] == '':
                shutil.rmtree(path)            
            else:
                os.remove(path)
