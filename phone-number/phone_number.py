import re
def Phone(Phone):
    Phone = str(Phone)
    Phone = re.sub('[^0-9]','',Phone)
    Phone = Phone[len(Phone)-10:len(Phone)]
    print(Phone)