# генерация результатов опроса

import random,time

M = 'м'
W = 'ж'

woman_names, surnames, man_names, songs = [],[],[],[]

try:
    fsongs = open('task/songs.txt')
    fnames_w = open('task/female_names.txt')
    fnames_m = open('task/male_names.txt')
    fsurnames = open('task/surnames.txt')
except IOError:
    print('Ошибка чтения файла')

for song in fsongs:
	songs.append(song.strip())	
for surname in fsurnames:
	surnames.append(surname.strip())
for name in fnames_m:
	man_names.append(name.strip())
for name in fnames_w:
	woman_names.append(name.strip())

fsongs.close()
fnames_m.close()
fnames_w.close()
fsurnames.close()
start = time.clock()
# секция генерации опроса
fw = open('interview.txt','w')                     
for surname in surnames:#250 фамилий
	for name in man_names:#143 имени
		age = random.randint(15,55)
		favors = []
		for i in range(5):
			favors.append(random.choice(songs))
		print("{0} {1}:{2}:{3}:{4}".format(name,surname,M,age,"|".join(favors)),file=fw)
	for name in woman_names:#136 имен
		age = random.randint(15,55)
		favors = []
		for i in range(5):
			favors.append(random.choice(songs))
		print("{0} {1}:{2}:{3}:{4}".format(name,surname+'а',W,age,"|".join(favors)),file=fw)
fw.close()		
end = time.clock()
print('Time: {0} s'.format(end - start))
