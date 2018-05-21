# формирование отчета

def form_report(fname,fout):
        fr = open('../results/'+fname)
        category = None
        if fname.startswith('male'):
                category = 'представителей сильного пола'
        elif fname.startswith('female'):
                category = 'представителей слабого пола'
        elif fname.startswith('ge'):
                category = 'лиц старше 20'
        else:
                category = 'лиц младше 20'
        print('<h1>TOP 10 композиций у '+category+'</h1>','<ol>',sep='\n',file=fout)	
        for song in fr:
                print('<li>{0}</li>'.format(song.strip()),file=fout)
        print('</ol>',file=fout)
        fr.close()

fw = open('report2.html','w',encoding='ISO-8859-5')
print('<html>',
      '<head><title>TOPs-10</title><head>',
      '<body>',sep='\n',file=fw)
form_report('male.txt',fw)
form_report('female.txt',fw)
form_report('ge20.txt',fw)
form_report('less20.txt',fw)
print('</body>','</html>',sep='\n',file=fw)
fw.close()

