''' Image downloader by Lyndon Chang '''

#imports
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

#create the search list
search = [ ] 

#ask for how many different types of images and number
types = int(input("Enter number of items: "))
limit = int(input("Enter number of images per item: "))

#input loop
x = 0;
while x < types:
    new = str(input("What do you want images of? "))
    search.append(new)
    x+=1;

#function
def downloadimages(query):
    arguments = {"keywords":query,
                 "format":"jpg", #jpg, gif, png, bmp, raw
                 "limit":limit,
                 "print_urls":True,
                 "size":"medium", #large, medium, icon
                 "aspect_ratio":"wide" #tall, square, wide, panoramic
                }
    try: 
        response.download(arguments)

    except FileNotFoundError:
        arguments = {"keywords":query,
                     "format":"jpg", 
                     "limit":limit,
                     "print_urls":True,
                     "size":"medium"
                     }
        try:
            response.download(arguments)
        except:
            pass

#driver code
for query in search:
    downloadimages(query)
    print("\033[1;32;40m--- Images have been downloaded ---\033[0m")
