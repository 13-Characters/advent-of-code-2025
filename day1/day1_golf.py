def part_1(input):
    return (lambda x:sum([(sum(x[:i])+50)%100==0for i in range(len(x))]))([int(l[1:].strip())*(1 if"R"in l else-1)for l in open(input)])
def part_2(input):
    return (lambda n: sum([len(set(range(z:=(sum(x)+50)%100,z+y+(a:=1if y>0else-1),a))&set(range(0,z+y,100*a))) for x, y in zip([n[0:i] for i in range(len(n))], n)]))([int(l[1:].strip())*(1 if"R"in l else-1) for l in open(input)])
if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))