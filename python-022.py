#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单

'''
a = ['a', 'b', 'c']
b = ['x', 'y', 'z']
L = []
for i in range(3):
    for j in range(3):
        L.append(a[i] + b[j])
L.remove('ax')
L.remove('ay')
L.remove('by')
L.remove('bz')
L.remove('cx')
L.remove('cz')
print(L)
