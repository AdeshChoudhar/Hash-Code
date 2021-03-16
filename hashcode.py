with open("f.txt") as f:
        lines = f.readlines()

D, I, S, V, F = list(map(int, lines[0].split()))

graph_elements = dict()
graph_elements_out = dict()
street = dict()
path = dict(); counter = 0; indeg = []
time = 0

for q in range(I):
    indeg.append(0)
for i in range(1, S + 1):
    B, E, street_name, L = lines[i].split()
    B, E, L = int(B), int(E), int(L)
    street[street_name] = [B,E]

    if E not in list(graph_elements.keys()):
        graph_elements[E] = []
    indeg[E] +=1
    graph_elements[E].append([B, street_name, L])
    if B not in list(graph_elements_out.keys()):
        graph_elements_out[B] = []
    graph_elements_out[B].append([E, street_name, L])

for i in range(S + 1, S + V + 1):
    input = lines[i].split()
    P, streets_required = input[0], input[1:]; P = int(P)
    path[counter] = [P, streets_required]
    counter +=1

# vertex or intersections attributes. 0: 0 is the red color, default. green = 1. [] is the queue. 
intex = dict()
for i in range(I):
    intex[i] = []
    intex[i].append([0,[], indeg[i]])
 
car = dict() #finding paths.
for j in range(counter):
    car[j]=[]
    for q in range(path[j][0]):
        car[j].append( street[path[j][1][q]][0] )
    car[j].append(street[path[j][1][q-1]][1] )
    intex[car[j][0]][0][1].append([[time],[j]]) #timestamp of car j when its at our vertex/intex.
dealtIntex = 0 #counter to check how many intex's schedule made.

schedule =dict() # its a list of pairs ( streetname, duration), both strings so I can write it to OP file.
for i in range(I):
    schedule[i]=[]
    for z in range(indeg[i]):
        schedule[i].append([graph_elements[i][z][1], str(1)])
    
opfile = open("schedule.txt","w"); s = "\n";
dealtIntex = I
opfile.write(str(dealtIntex))
opfile.write(s)
for z in range(I):
    opfile.write(str(z)) #Name of vertex
    opfile.write(s) #newline
    opfile.write(str(indeg[z])) #It's indeg for now.. but it has to be indeg so tht light turns green for them
    opfile.write(s)                         #loop to consider multiple incoming edges.
    for w in range(indeg[z]):
        opfile.write(schedule[z][w][0]) #edge or street name
        opfile.write(" ")
        opfile.write(schedule[z][0][1]) #duration
        opfile.write(s)
opfile.close()
