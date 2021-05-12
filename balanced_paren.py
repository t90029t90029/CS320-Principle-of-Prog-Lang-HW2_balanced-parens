# balanced paren

# Shang Chun Lin : HW2
def balanced_paren(str):
    # +++your code here+++
    n = len(str)
    count = 0
    if n == 0:
        print("True, it's an empty sequence")
        return
    for k in str:
        if k == '[':
            count += 1
        else :
            count -= 1

        if count < 0 :
            break

    if count < 0 :
        print("False")
    else :
        print("True")
    return

if __name__ == "__main__":
    balanced_paren('')          #True
    balanced_paren('[[]]')      #True
    balanced_paren('[[]]]')     #False
    balanced_paren('[]][[]')    #False
    balanced_paren('[[][]]')    #True
