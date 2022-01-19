def Area_triangle(a,b):
    return a*b/2

def Area_rectangle(a,b):
    return a*b

def Area_square(a):
    return a*a

def area(figure,a,b=1):
    areas = {
        "90_degree_triangle": Area_triangle(a,b), 'square': Area_square(a), 'rectangle':Area_rectangle(a,b)
    }

    return areas[figure]

print(area("square",3))
print(area("rectangle",3,4))
print(area("90_degree_triangle",3,4))

