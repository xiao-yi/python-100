'''
题目：有n个整数，使其前面各数顺序向后移m个位置，
最后m个数变成最前面的m个数
n=8 m=5
如原始列表: [2, 8, 6, 1, 78, 45, 34, 2]
移动之后: [1, 78, 45, 34, 2, 2, 8, 6]
'''
n = list(input('请输入n个数(空格分隔):').split())
m = int(input('请输入移动的m(m<n)：'))
print(n[m:len(n)]+n[:m])
