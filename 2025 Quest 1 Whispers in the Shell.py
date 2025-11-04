
# 4/11/25


# Part 1
names = ['Phyrophis','Wynxelor','Felnoris','Anorkynar','Marendris','Durnnixis','Ryssris',\
          'Mornthyn','Balthmir','Jalmirath']

code = 'L9,R4,L5,R7,L2,R5,L1,R9,L9,R2,L9'
n = 0

for i in range(0, len(code), 3):
    if code[i] == 'L':
        n -= int(code[i+1])
    else:
        n += int(code[i+1])
    if n < 1:
        n = 0
    elif n > len(names)-1:
        n = len(names)-1

print(names[n])


# Part 2
names = ['Thalisis','Ryssquin','Iskararis','Pylartal','Ignmirix','Jaror','Anorix',\
         'Urithirin','Kalix','Orahnylor','Ulkvash','Urakimar','Nylvynar','Kronynn',\
         'Xilhal','Brynkryth','Lazgoril','Dordaros','Thazlon','Braenylor']

code = 'L13,R5,L8,R5,L11,R8,L6,R8,L15,R7,L5,R6,L5,\
        R18,L5,R7,L5,R8,L5,R17,L19,R18,L8,R18,L14,R15,L13,R11,L17'
n = 0
i = 0
val = 0
while i < len(code)-1:
        
    if code[i].isdigit() == False and code[i] != ',':
        
        if code[i] == 'L':
            val = code[i+1]
            if code[i+2].isdigit() and i+2 < len(code):
                val += code[i+2]
            n -= int(val)
            
        elif code[i] == 'R':
            val = code[i+1]
            if code[i+2].isdigit() and i+2 < len(code):
                val += code[i+2]
            n += int(val)
    
    i += 1

if n > len(names):
    n = i % len(names)
print(names[n])


# Part 3
names = ['Ilmarsarix','Nythwyris','Wynlar','Ignhal','Morsarix','Arvral','Cyndernyn',\
         'Sorurath','Lirdrith','Quarnpyxis','Harjoris','Hyravor','Havtaril','Drelxel',\
         'Arvbryn','Zorfelix','Raelvynar','Xilcarth','Fyndeth','Belzar','Lazynn',\
         'Urithvalir','Ulmarzral','Quenther','Drelacris','Gaergyth','Rythansyron',
         'Xarorath','Drethiral','Olarcalyx']

code = 'L36,R33,L7,R13,L14,R5,L44,R45,L37,R16,L27,R6,L6,R8,L19,R30,L20,R27,L41,R11,L5,R46,L5,R37,L5,R49,L5,R6,L5,R28,L5,R5,L5,R23,L5,R8,L5,R49,L5,R11,L8,R42,L38,R25,L44,R37,L30,R21,L10,R14,L37,R26,L13,R47,L42,R45,L26,R39,L8'

i = 0
val = 0
spare = 0

while i < len(code)-1:
    n = 0
    if code[i].isdigit() == False and code[i] != ',':
        if code[i] == 'L':
            val = code[i+1]
            if i+2 < len(code):
                if code[i+2].isdigit():
                    val += code[i+2]
            n -= int(val)
            
        elif code[i] == 'R':
            val = code[i+1]
            if i+2 < len(code):
                if code[i+2].isdigit():
                    val += code[i+2]
            n += int(val)

        # n is the index of the chosen name
        if n > len(names)-1:
            n = n % len(names)
        elif n < 0 - len(names):
            n += 30
            
        spare = names[0]
        names[0] = names[n]
        names[n] = spare
    
    i += 1

print(names[0])








