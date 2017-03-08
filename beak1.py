'''
예제 입력  복사
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
예제 출력  복사
300
864
'''



#chapters = [1, 21, 3, 4, 5, 35, 5, 4, 3, 5, 98, 21, 14, 17, 32]
chapters = [40, 30, 30, 50]

sum = 0
for i in range(len(chapters)):
    chapters.sort()
    print chapters
    
    if len(chapters) == 2:
        sum += chapters[0]
        sum += chapters[1]
        break
        
    two_chapter = chapters[0] + chapters[1]
    print chapters[0], 'and', chapters[1], 'merged'
    sum += two_chapter
    print chapters[0] , 'deleted'
    del chapters[0]
    print chapters[0], 'deleted'
    del chapters[0]
    chapters.append(two_chapter)
    print '\n'

print sum
