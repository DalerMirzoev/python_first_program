            #simplest version
#x = int(input("What's x? "))
#if x%2==0:
#    print('Even')
#else:
#    print('Odd')

            #using def
#def even(n):
#   if n%2==0:
#       return True
#   else:
#       return False

            #makung def more succint
#def even(n):
#   return True if n%2==0 else False

def main():
    x = int(input("What's x? "))
    if even(x):
        print('Even')
    else:
        print('Odd')

def even(n):
    return n % 2==0

main()