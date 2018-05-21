# обработка результатов опроса по 4 категориям

import time

def category_info(fr,fname_w):    
    rate = {}
    for line in fr:    
        ss = line.split(':')            
        # ранжирование песен по популярности
        factor = 1 # коэффициент популярности
        for x in ss[3].split('|'):
            x = x.strip()
            rate[x] = round(rate.get(x,0) + factor,2)            
            factor -= 0.2
    l = list(rate.items())
    l.sort(key=lambda x:x[1],reverse=True)
   
    fw = open(fname_w,'w')
    for i in range(10):
        print(l[i][0],file=fw)
    fw.close()

start = time.clock()
try:
    male = open('male.txt')
    female = open('female.txt')
    ge20 = open('ge20.txt')
    less20 = open('less20.txt')
    
    category_info(male,'results/male.txt')
    category_info(female,'results/female.txt')
    category_info(ge20,'results/ge20.txt')
    category_info(less20,'results/less20.txt')
except IOError:
    print('Ошибка чтения файла')

male.close()
female.close()
ge20.close()
less20.close()

end = time.clock()
print('Time: {0} s'.format(end - start))
