from collections import deque  #Also in 'collections'.

mydq = deque([1,2,3,4,5])
print(mydq)

print(mydq.popleft())           #Pops first object.
print(mydq)

print(mydq.pop())               #Pops last object.
print(mydq)

print(list(mydq))               #Also can be list.