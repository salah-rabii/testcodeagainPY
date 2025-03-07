# palindrome.py

def palindrome(ch):
    
    ch = ch.replace(" ","").lower()
   
    
    
    i = 0
    j = len(ch) - 1
    print(j)

    while i < j:
        if ch[i] != ch[j]:  
            return False
        i += 1
        j -= 1
    return True  


def main():
    
    chaine = input("Entrez un mot: ")

    if palindrome(chaine):
        print(f"{chaine} est un palindrome.")
    else:
        print(f"{chaine} n'est pas un palindrome.")

main()