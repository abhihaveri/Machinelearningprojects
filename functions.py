## why functions ?(Interview questions)
# 1. to make code more readable.
# 2. to make code more efficient.
# 3. to make code more maintabinable.
# 4. to make code more reusable.
# 5. to make code more extensible.

# function 
def welcome(msg)->str:
    return msg

msg=welcome("welcome All")
print(msg + "\nPlease subscribe")



### Functions to add Evrn and Odd Number s

def even_odd_sum(lst):

    even_sum=0
    odd_sum=0

    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum,odd_sum

sum1,sum2=even_odd_sum([1,2,3,4,5,6,7,8,9,10,11,12])
print(f"The Even_sum is {sum1} and Odd Sum is {sum2}")