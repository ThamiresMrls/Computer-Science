def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
        print better
    return approx
sqrt(25)
def print_triangular_numbers(n):
    i=2
    j=1
    r=1
    while n !=0 :
        print j, '\t', r
        r=r+i
        i +=1
        j +=1
        n =n-1
print_triangular_numbers(100)
