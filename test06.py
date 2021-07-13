
try:
    f=open('./data/readme.txt', mode='r', encoding='utf-8')
    f2=open('./data/writeme.txt', mode='w', encoding='utf-8')
    line = f.readline()
    while line:
        print(line)
        f2.write(line)
        line=f.readline()

    f2.write('add text')
    f.close()
    f2.close()

    print('file modify sucess')
except Exception as e:
    print('exception : {0}'.format(e))