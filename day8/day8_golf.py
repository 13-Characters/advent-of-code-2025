def part_1(fp):
    pairs = (lambda p: sorted([divmod(i,len(p)) for i in range(len(p)**2) if i//len(p)<i%len(p)],key=lambda a:sum((y-x)**2 for x,y in zip(p[a[0]],p[a[1]]))))([eval(l) for l in open(fp)])
    c = [{i} for i in len(open(fp).readlines())]
    for k in pairs[0:1000]:
        pass

def part_2(fp):
    pass
if __name__ == "__main__":
    part_1("input")