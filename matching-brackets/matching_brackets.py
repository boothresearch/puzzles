def is_paired(input_string):
    count = 0
    for i in input_string:
        if i == "(":
            count = count + 1
            print(count)
        elif i == ")":
            count = count -1 
            print(count)
            
    if count == 0 :
        print("all paired")
    else:
        print("not paired")
        
    