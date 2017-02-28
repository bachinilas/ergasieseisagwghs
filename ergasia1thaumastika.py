print "Plhktrologeiste mia protash"
t1=raw_input()
megethos=len(t1)
point=1
m1=megethos
while (megethos>0) and (point==1):
        megethos=megethos-1
	if t1[megethos]!=("!"):
                point=0
		m1=megethos
m1=m1+1	
t2=t1.replace("!","")
t2=t2+((len(t1)-m1)*"!")
print t2
	 
