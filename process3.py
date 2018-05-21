# вывод респондентов, поставивших на 1 место одну из трёх композиций,
# наиболее популярных в их категории 

import time

def category_respondents(fpopular,fin,fout):
    popSong = []
    for i in range(3):
        popSong.append(fpopular.readline().strip())
        
    fw = open(fout,'w')
    for line in open(fin):
        ss = line.split(':')
        if ss[3].split('|')[0] in popSong:
            print(ss[0],file=fw)    
    fw.close()            

start = time.clock()
try:
    fwoman = open('results/female.txt')
    fman = open('results/male.txt')
    fge20 = open('results/ge20.txt')
    fless20 = open('results/less20.txt')

    category_respondents(fwoman,'female.txt','results/womanNames.txt')
    category_respondents(fman,'male.txt','results/manNames.txt')
    category_respondents(fge20,'ge20.txt','results/ge20Names.txt')
    category_respondents(fless20,'less20.txt','results/less20Names.txt')
except IOError:
    print('Ошибка чтения файла')

fwoman.close()
fman.close()
fge20.close()
fless20.close()

end = time.clock()
print('Time: {0} s'.format(end - start))
