# fast return / quick exit
def solveQuadratic(a, b, c):
    if (a == 0 and b == 0 and c == 0):
        return "Everything"

    if(a == 0 and b == 0 and c != 0):
        return "None"

    if (a == 0):
        return -c/b

    delta = b ** 2 - 4 * a * c
    if (delta < 0):
        return "None"

    if (delta == 0):
        return -b / (2 * a)
    
    result_dict = {}
    import math
    result_dict.update({"x1": (-b + math.sqrt(delta)) / (2 * a)})
    result_dict.update({"x2": (-b - math.sqrt(delta)) / (2 * a)})
    return result_dict


# a = int(input())
# b = int(input())
# c = int(input())
# result = solveQuadratic(a, b, c)
# print(result)

print(solveQuadratic(1, 2, -3))