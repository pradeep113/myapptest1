from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys


def button(request):
    return render((request), 'home.html')


#def output(request):
#    data = requests.get('https://w3schools.com/python/demopage.htm')
#    print(data.text)
#    data = data.text
#    return render(request, 'home.html', {'data': data})


def external(request):
    inp = request.POST.get('param')
    #out = run([sys.executable,'//Users//pradeepkumar//MyOfflineDocs//PYTHON_PROJ//DJANGO//buttonpython//test.py',inp],shell=False,stdout=PIPE)
    # print(out)

    f = open('scopefile.txt', 'w')
    fres = open('result.txt', 'r')
    contents = fres.read()
    print(inp)
    print(contents)
    f.write(inp)
    # return render(request,'home.html',{'data1':out.stdout})

    return render(request, 'home.html', {'data1': contents})
