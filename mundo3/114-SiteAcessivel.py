'''
 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('Este site não está acessível no momento!')
else:
    print('Este site está acessível no momento!')
    #print(site.read()) =>pega o código do site