imageFileTypes = ['.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif', '.webp', '.tiff', '.tif', '.psd', '.raw', '.arw', '.cr2', '.nrw',
                  '.k25', '.bmp', '.dib', '.heif', '.heic', '.ind', '.indd', '.indt', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.svg', '.svgz', '.ai', '.eps']

# create an array of common video file types
videoFileTypes = ['.webm','.mpg','.mp2','.mpeg','.mpe','.mpv','.ogg' ,'.mp4','.m4p','.m4v','.avi','.wmv','.mov','.qt','.flv','.swf','.avchd']

# join checked file types
def joinLists():
    list = []
    if 1 == 1:
        for i in imageFileTypes:
            list.append(i)  
    if 1 == 1:
        for i in videoFileTypes:
            list.append(i)
    return list

print(joinLists())