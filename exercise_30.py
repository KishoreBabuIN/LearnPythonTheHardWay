people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print"That's too many busses."
elif buses < cars:
    print "Maybe we could take the busses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the busses."
else:
    print "Fine, let's stay home then."