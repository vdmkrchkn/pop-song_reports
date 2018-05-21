# обработка результатов опроса

from collections import Counter
import time

rate = {}
cnt = Counter()

male = open('male.txt','w')
female = open('female.txt','w')
less20 = open('less20.txt','w')
ge20 = open('ge20.txt','w')
start = time.clock()
try:
    interview = open('interview.txt') 
    for line in interview:    
        ss = line.split(':')    
        # разделение респондентов по половому признаку
        if ss[1] == 'м':
            print(str(line.strip()),file=male)
        else:
            print(str(line.strip()),file=female)
        #  разделение респондентов по возрастному признаку
        try:
            age = int(ss[2])    
        except ValueError:
            print('Некорректный формат файла')
        if age < 20:
            print(str(line.strip()),file=less20)
        else:
            print(str(line.strip()),file=ge20)
        # ранжирование песен по популярности
        factor = 1 # коэффициент популярности
        for x in ss[3].split('|'):
            x = x.strip()
            rate[x] = round(rate.get(x,0) + factor,2)
            cnt[x] += 1
            factor -= 0.2
except IOError:
    print('Ошибка чтения файла')
    
interview.close()
male.close()
female.close()
less20.close()
ge20.close()

frating = open('results/popularSongs.txt','w')

# сортировка по значению
for key, value in sorted(rate.items(),key=lambda k:k[1],reverse=True):
    print(str(key).ljust(88),format(value,"4.1f"),cnt[key],file=frating)    

frating.close()
end = time.clock()
print('Time: {0} s'.format(end - start))   

