import os ,sys 
Directory=sys.argv[1]

home=os.environ["HOME"]

if not os.path.isabs(Directory):
    Directory=os.path.join(home,Directory)

if not os.path.isdir(Directory):
    print("PLEASE ENTER A VALID DIRECTORY OR DIRECTORY PATH")
    exit()

print(f"Directory : {Directory} \n\n")

folders=['Images','Videos','Audio','Documents','Others']
for f in folders:
    os.mkdir(os.path.join(Directory,f))

imgEXT=['.jpg','.png','.webp','.gif','.svg','.jpeg']
vidEXT=['.mp4','.mkv','.avi','.webm','.wmv']
audEXT=['.mp3','.m4a','.aac','.ogg','.flac']
docuEXT=['.txt','.docx','.pdf','.odt','.pptx','.ppt','.csv']

items=[]
get_file=os.listdir(Directory)

for i in get_file:
    check=os.path.join(Directory,i)
    if not os.path.isdir(check):
        items.append(i)

for item in items:
    _,exe=os.path.splitext(item)
    if exe in  imgEXT:
        os.rename(os.path.join(Directory,item),os.path.join(Directory,'Images',item))

    elif exe in  vidEXT:
        os.rename(os.path.join(Directory,item),os.path.join(Directory,'Videos',item))

    elif exe in  audEXT:
        os.rename(os.path.join(Directory,item),os.path.join(Directory,'Audio',item))

    elif exe in  docuEXT:
        os.rename(os.path.join(Directory,item),os.path.join(Directory,'Documents',item))

    else:
        os.rename(os.path.join(Directory,item),os.path.join(Directory,'Others',item))

print("Files Moved Sucessfully")