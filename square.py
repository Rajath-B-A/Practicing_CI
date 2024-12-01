def square_num(a):
    return a*a

def prime(a):
    if a>1:
        for i in range(2,(a//2)+1):
            if i%2==0:
                return "No"
        else:
            return "Yes"
    else:
        return "No"
