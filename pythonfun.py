year=int(input("ENTER THE NUMBER"))
def is_leap(year):
    if(year%4==0) or (year%1!=0):
        return True


    return False


if is_leap(year):
    print("YEAR IS LEAP")
else:
    print("YEAR IS NOT AN LEAP")
