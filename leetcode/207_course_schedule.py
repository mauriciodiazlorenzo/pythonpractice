numCourses=4
prerequisites = [[0,1],[3,1],[1,3],[3,2]]


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    descendents = [set() for x in range(numCourses)]
    for x in prerequisites:
        descendents[x[0]].add(x[1])
    for n in range(numCourses):
        alldesc = descendents[n]
        nextdesc = set()
        depth = 0
        while alldesc:
            if depth>numCourses:
                return False
            for i in alldesc:
                if i==n:
                    return False
                nextdesc.update(descendents[i])
            alldesc=nextdesc
            nextdesc=set()
            depth+=1
    return True

canFinish(numCourses,prerequisites)