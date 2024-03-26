def list_comprehension(listA):
    return [listA[x] + listA[x+1] for x in range(len(listA)-1) if len(listA)>1]