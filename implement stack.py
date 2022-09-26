Stack = []
top = None

def isEmpty(stck):
    if(stck==[]):
        return True
    else:
        return False
    
def push(stck, item):
    global top
    stck.append(item)
    top=len(stck)-1
    
def s_pop(stck):
    global top
    if(isEmpty(stck)):
        return('underflow')
    else:
        i=stck.pop()
        if (len(stck)==0):
            top=None
        else:
            top=top-1
    return i

def peek(stck):
    if(isEmpty(stck)):
        return('underflow')
    else:
        top=len(stck)-1
        return stck[top]

def display(stck):
    if(isEmpty(stck)):
        print('Heyy! Stack is empty!')
    else:
        top=len(stck)-1
        print(stck[top],'<-- top')
        
        for i in range(top-1,-1,-1):
            print(stck[i])
            
while True:
    print('Implementation of STACK')
    print('1. Push')
    print('2. Peek')
    print('3. Display')
    print('4. Pop')
    print('5. Exit')
    
    Option =int(input('Enter an option in (1-5): '))
    if(Option==1):
        item = input('Enter the string that you want to push:')
        push(Stack,item)
        print('%s added successfully' %item)
        input ('Press any key to continue...')

    elif(Option==2):
        item =peek(Stack)
        if (item=='underflow'):
            print('stack is already empty!')
        else:
            print('%s is at the top' %item)
            input ('Press any key to continue...')  
    
    elif(Option==3):
        display(Stack)
        input ('Press any key to continue...')

    elif(Option==4):
        item =s_pop(Stack)
        if (item=='underflow'):
            print('stack is already empty!')
        else:
            print('%s is popped' %item)
            input ('Press any key to continue...') 
            
    elif(Option==5):
        break
        
    else:
        print('Invalid option')
        input ('Press any key to continue...')
    print('\n\n')
        