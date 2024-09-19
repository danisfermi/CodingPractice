# Bipartite Matching

'''
questions[
{id:1, tags: ["MAC", "VSCODE"]},
{id:2, tags: ["PY", "AI"]}
{id:3, tags: ["JAVA", "OS"]}
{id:4, tags: ["PY", "NW"]}
]

Volunteer[
{id: "1", tags:["PY",""NW], name: "A"},
{id: "2", tags:["AI"], name: "B"},
{id: "3", tags:["JAVA","NW], name: "C"},
{id: "4", tags:["JAVA","NW"], name: "D"}
]

Assign question to volunteers such that each question is assigned to at most one volunteer based on tags match.
One volunteer can take at most one question and maximise the question assigned to volunteer.

for this example
A can take question 4(PY match)
B can take question 2(AI match)
C can take question 3(Java match)
Question one no one can take as not match.
'''

questions = [
					{"id": 1, "tags": ["MAC", "VSCODE"]}, 
					{"id": 2, "tags": ["PY", "AI"]},
					{"id": 3, "tags": ["JAVA", "OS"]},
					{"id": 4, "tags": ["PY", "NW"]}
				]

volunteers = [
					{"id": 1, "tags":["PY","NW"], "name": "A"},
					{"id": 2, "tags":["AI"], "name": "B"},
					{"id": 3, "tags":["JAVA","NW"], "name": "C"},
					{"id": 4, "tags":["JAVA","NW"], "name": "D"}
				]

graph = [[0] * len(volunteers) for _ in range(len(questions))]
for question in questions:
    for volunteer in volunteers:
        if len(set(question['tags']).intersection(set(volunteer['tags']))) != 0:
            graph[question['id']-1][volunteer['id']-1] = 1

ans = [-1] * len(graph[0])
def canMatch(q, visited):
    for v in range(len(graph[0])):
        if graph[q][v] != 1:
            continue
        if v in visited:
            continue
        visited.add(v)
        if ans[v] == -1 or canMatch(ans[v], visited):
            ans[v] = q
            return True
    return False

count = 0
for q in range(len(graph)):
    visited = set()
    if canMatch(q, visited):
        count += 1
matching = ["Question " + str(ans[i] + 1) + " -> " + "Volunteer " + str(volunteers[i]["name"]) \
			if ans[i] != -1 else '' for i in range(len(ans))]
print(matching)
