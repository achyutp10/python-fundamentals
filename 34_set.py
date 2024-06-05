# Iterable, unordered, no duplicates, growable, mutable
# s1 = {"Jack", 45, 38.5, True}
# s2 = set((1,2,3,4))
# print(s2)
# s3 = set('Python')
# print(s3)
# s3.discard('P')
# print(s3)
# s3.add(120)
# print(s3)
# print(len(s3))

# A={1,2,3,5,7} 
# B={5,7,9,10,11}
# # print(A.union(B))
# # print(A.intersection(B))
# # print(A.difference(B))
# # print(A.symmetric_difference(B))

# s = { 1,2,3,4,5,6,7,8,9,10 }
# C = A | B
# C = A & B
# C = A - B
# C = A ^ B 

s = set()
s1 = {x for x in range(10)}
s2 = {x**2 for x in [-2,-1,0,1,2]}
s3 = {x for x in (10,5,7,8,12,3) if x%2==0}
s4 = {X.upper() for X in 'philippines'}