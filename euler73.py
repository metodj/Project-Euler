
def euler72(n):
    resitev = set()
    for imenovalec in range(1, n + 1):
        for stevec in range(1, imenovalec):
            if (1 / 3) < (stevec / imenovalec) < (1 / 2):
                resitev.add(stevec / imenovalec)
    return len(resitev)