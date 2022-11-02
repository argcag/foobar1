#foobar 1
#algorithmic approach:
#if we have a list (">---<><") we only need to consider 1 direction of movement
#(for this example i will only look at the left facing arrows, and simply check how many right facing arrows are on the left of each, add 2 for each).

def solution(hallway):
    salutes = 0
    for i in range(0,len(hallway)): #range = the whole list
        if hallway[i] == "<":
            for j in range(0,i): #range = the list up to where the left facing arrow is
                if hallway[j] == ">": 
                    salutes += 2
    return salutes

print(solution("<><>---><<"))
