import math
books = [1, 5, 6, 6, 8, 13, 14, 18]
mean = sum(books) / len(books)
variance = sum((x - mean) ** 2 for x in books) / len(books)
std_dev = math.sqrt(variance)

print(len(books))
print(sum(books))
print(mean)
print(variance)
print(std_dev)