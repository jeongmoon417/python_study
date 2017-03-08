#chapters = [1, 21, 3, 4, 5, 35, 5, 4, 3, 5, 98, 21, 14, 17, 32]
chapters = [40, 30, 30, 50]

sum = 0
for i in range(len(chapters)):
    chapters.sort()
    if len(chapters) == 1:
        break
    two_chapter = chapters[0] + chapters[1]
    print chapters[0], 'and', chapters[1], 'merged'
    sum += two_chapter
    print chapters[0] , 'deleted'
    del chapters[0]
    if (len(chapters) > 1):
        print chapters[0], 'deleted'
        del chapters[0]
    chapters.append(two_chapter)
    print chapters

print sum