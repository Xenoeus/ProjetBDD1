def verificationParenthesis(code):
    listeParenthesis = []
    for lettre in code:
        if(lettre == '('):
            listeParenthesis.append(lettre)
        elif(lettre == ')'):
            if(len(listeParenthesis) == 0):
                print(code)
                print('il manque une/des parenthèse(s) ouvrante')
                return False
            elif(listeParenthesis[-1] != '('):
                print(code)
                print('il manque une/des parenthèse(s) ouvrante')
                return False
            else:
                del listeParenthesis[-1]
            
        
    
    if(len(listeParenthesis)>0):
        print(code)
        print('il manque une/des parenthèse(s) fermante')
        return False
    
    return True
    
