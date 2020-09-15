import re 
def Phone(phone):
    #Turn into string if it is not already
    phone = str(phone)
    #Remove everything but numbers
    phone = re.sub('[^0-9]','', phone)
    #Keep last 11 numbers
    phone = phone[len(phone)-10:len(phone)]
    #Print
    return phone

