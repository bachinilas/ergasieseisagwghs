print "Plhktrologhse mia akolouthia parenthesewn"
text=raw_input()
keimeno=len(myList)
swsto = ['(', '(', ')', ')']
lathos   = [')', '(', ')', '(']
def check_mathematical_order(myList):
    opened = 0
    closed = 0
    change_shifts = False
    while keimeno > 0:
        poped_item = myList.pop()
        if poped_item  == ')' and not change_shifts:
            closed += 1
        elif poped_item  == ')' and change_shifts:
            print( check_mathematical_order(lathos) )
            return False
        elif poped_item  == '(':
            print( check_mathematical_order(swsto) )
            change_shifts = True
            opened += 1
    return opened == closed
