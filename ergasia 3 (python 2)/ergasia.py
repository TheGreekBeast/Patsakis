with open('paradeigma.py', 'r') as before: #den hmoun sigouros an eprepe to onoma tou arxeiou na einai input apo ton xrhsth h oxi opote to ekana etsi poy einai pio eukolo
    lines = before.readlines()

with open('p4.py', 'w') as after:
    for line in lines:
        if line.strip():
            line = line.split('#')
            newline = line[0].rstrip()
            if newline:
                after.writelines(newline)
                after.writelines('\n')


        
            
