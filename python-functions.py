# 1

def sum_to(n):
    return sum(range(1, n+1))

print(sum_to(10))


# 2

def largest(list):
    return max(list)

print(largest([10, 4, 2, 231, 91, 54]))

# 3

def occurances(str1, str2):
    return str1.count(str2)

print(occurances('fleep floop', 'p')) 

# 4

def product(*nums):
    acc = 1
    for n in nums:
        acc *= n
    return acc

print(product(2, 5, 5) )
