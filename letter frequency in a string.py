# p = []
# j = {}
# def count_letters (n):
#     for i in n:
#         if i in p:
#             pass
#         else:
#             p.append(i)
#     p.sort()
#     for u in p:
#         a = n.count(u)
#         j[u] = a

# count_letters('hello')
# print (j)





# p = []
# j = {}
# def count_letters (n):
#     alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for k in alpha:
#         j[k] = 0
#     n = n.upper()
#     for i in n:
#         if i in p or not(i in alpha):
#             pass
#         else:
#             p.append(i)
#     for u in p:
#         a = n.count(u)
#         j[u] = j[u] + 1

# count_letters('The quick brown fox jumps over the lazy dog')
# print (j)



# def count_letters (n):
#     d = {}
#     for i in n:
#         d[i] = d.get(i, 0) + 1
#     return d

# print (count_letters('A quick brown fox jumped over a lazy dog'))



# p = []

# d = {}
# def letter (s):
#     q = []
#     s = s.upper()
#     for i in s:
#         if i in p or i == ' ':
#             pass
#         else:
#             # a = s.index(i)
#             # print (a)
#             p.append(i)
#     p.sort()
#     for k in p:
#         for u in s:
#             if k == u:
#                 a = s.index(k)
#                 b = s.count(k)
#                 if a in q:
#                     pass
#                 else:
#                     q.append(a)
#                     q.append(b)
#             else:
#                 pass
#         d[k] = q
#         q = []

#     return (d)

# print (letter ('A quick brown fox jumped over a lazy dog'))