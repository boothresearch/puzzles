import re 
def Phone(phone):
    phone = str(phone)
    phone = re.sub('[^0-9]','', phone)
    phone = phone[len(phone)-10:len(phone)]
    
    print(phone)
    #def __init__(self, phone_number):
    #    pass
