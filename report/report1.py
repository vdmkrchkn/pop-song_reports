# формирование отчета

fr = open('../results/popularSongs.txt')
fw = open('report1.html','w',encoding='ISO-8859-5')
print('<html>',
      '<head><title>Список композиций в порядке популярности</title><head>',
      '<body>',
      '<h1>Список композиций в порядке популярности</h1>',
      '<ol>',sep='\n',file=fw)
for song in fr:
    print('<li>{0}</li>'.format(song.strip()),file=fw)
print('</ol>',
      '</body>',
      '</html>',sep='\n',file=fw)

fr.close()
fw.close()
