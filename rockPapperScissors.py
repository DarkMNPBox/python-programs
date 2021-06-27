import random

def computerChoice():
    choice = random.choice(['r','p','s'])
    print('computer Choice : ',choice)
    return choice
def myChoice():
    print('-'*30)
    choice = input('ENter your choice : ')
    if choice in ['r','p','s']:
        return choice
    else:
        print('Enter a valid move [r,p,s]')
        return myChoice()

def play(n):
    my_score = 0
    com_score = 0
    i=0
    while(i<n):
        my = myChoice()
        com = computerChoice()
        i+=1
        ch = my+com
        if ch in ['rs','pr','sp']:
            print('You got him !!!')
            my_score +=1
        elif ch in ['sr','rp','ps']:    
            print('You fucked !!!')
            com_score +=1
        else:
            print(' its a Draw !!!')        
    print('*'*50)       
    print('-'*8+' my_score : ',my_score,'   com_score : ',com_score,'-'*8)
    print('*'*50)         

if __name__ == '__main__':
    n = int(input('How many time you want to play : '))
    play(n)

        

