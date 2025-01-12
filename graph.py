#
#
#

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'D'
frontier = [start]
exploror = set()

print(frontier, exploror)

while len(frontier) > 0:
    current = frontier.pop()   
    print(current)
    
    if current == goal:
        print("Goalllllllll")
        break
    print(f"neighbor of {current} is {graph[current]}")
    for neighbor in graph[current]:
        frontier.append(neighbor)
