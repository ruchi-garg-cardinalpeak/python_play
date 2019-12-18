def spam():
    eggs = 'spam local'
    print(eggs)     #prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)    #prints 'bacon local'
    spam()
    print(eggs)     #prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)


#eggs = 42
#spam()
#print(eggs)




#def spam():
#    print(eggs)
#eggs = 42
#spam()
#print(eggs)
