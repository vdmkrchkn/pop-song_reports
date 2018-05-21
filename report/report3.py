# формирование отчета

def form_report(fname,fout):
        fr = open('../results/'+fname)
        category = None
        if fname.startswith('man'):
                category = 'представителей сильного пола'
        elif fname.startswith('woman'):
                category = 'представителей слабого пола'
        elif fname.startswith('ge'):
                category = 'лиц старше 20'
        else:
                category = 'лиц младше 20'
        print('<h1>TOP среди '+category+'</h1>','<ul>',sep='\n',file=fout)	
        for song in fr:
                print('<li>{0}</li>'.format(song.strip()),file=fout)
        print('</ul>',file=fout)
        fr.close()

fw = open('report3.html','w',encoding='ISO-8859-5')
print('<html>',
      '<head><title>Список самых крутых респондентов</title><head>',
      '<body>',sep='\n',file=fw)
form_report('manNames.txt',fw)
form_report('womanNames.txt',fw)
form_report('ge20Names.txt',fw)
form_report('less20Names.txt',fw)
print('</body>','</html>',sep='\n',file=fw)
fw.close()

