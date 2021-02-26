import graph

def solve(filename):
    with open(filename) as f:
        lines = f.readlines()

    D, I, S, V, F = list(map(int, lines[0].split()))

    graph_elements = dict()
    for i in range(1, S + 1):
        B, E, street_name, L = lines[i].split()
        B, E, L = int(B), int(E), int(L)

        if B not in list(graph_elements.keys()):
            graph_elements[B] = []
        graph_elements[B].append([E, street_name, L])
    
        print(graph_elements)

    for i in range(S + 1, S + V + 1):
        input = lines[i].split()
        P, streets_required = input[0], input[1:]
    


def output():
    f = open("output.txt","w")
    f.write("hello, world")
    f.close()


if __name__ == "__main__":
    solve("a.txt")
    output()
