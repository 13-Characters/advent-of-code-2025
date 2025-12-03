def part_1(fp):
    return sum(sum(i for i in range(*r)if(s:=str(i))[:len(s)//2]*2==s)for r in(tuple(map(int,y.split("-")))for y in open(fp).read().strip().split(",")))
def part_2(fp):
    return sum(sum(i for i in range(*r)if((s:=str(i))*2).find(s,1)!=len(s))for r in(tuple(map(int,y.split("-")))for y in open(fp).read().strip().split(",")))
print(part_1("input"))
print(part_2("input"))