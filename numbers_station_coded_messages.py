def answer(l, t):
    possible = list()
    for i in xrange(len(l)): # Iterate each starting index
        total = 0
        for j in xrange(len(l)): # Iterate rest of indexi
            if j < i: # If index <= start
                continue
            print total
            total += l[j]
            if total == t:
                possible.append({
                "start": i,
                "end": j,
                "length": j-i
                })
        print

    if not possible:
        return [-1, -1]

    smallest = 300
    for i in xrange(len(possible)):
        if possible[i]["length"] < smallest:
            smallest = i

    return [ possible[smallest]["start"], possible[smallest]["end"] ]
