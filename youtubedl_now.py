#coding: utf-8
from youtube_dl import YoutubeDL
import webbrowser
import sys
import urllib
import clipboard
import re
import console
import unicodedata

def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
	if unicodedata.category(c) != 'Mn')


choise = console.alert('Choose Quality','', 'Lowest', 'Medium', 'Best')

if choise==1:
	ydl = YoutubeDL({'quiet':True,'format':'36/5/43/18/22'})
elif choise==2:
	ydl = YoutubeDL({'quiet':True,'format':'18/135/43/134/133/160'})
elif choise==3:
	ydl = YoutubeDL({'quiet':True,'format':'best'})

console.show_activity()
console.clear()
print('Wait a Moment Please!')
link = clipboard.get()
#try to Download info
try:
	info = ydl.extract_info(link, download=False)
except:
	print('Trying with another video quality...')
	ydl = YoutubeDL({'quiet':True,'format':'best'})
	info = ydl.extract_info(link, download=False)
#print info['url']

download_url = info['url']
#print download_url

titulo = info['title']

#Codifico el titulo para URL
#elimino ascentos
titulo=strip_accents(titulo)
#elimino simbolos
titulo=re.sub(r'[^a-zA-Z0-9]','',titulo)

try: 
	titulo = urllib.quote_plus(titulo)
except:
	print 'Impossible to encode title'
	titulo = 'Video_Downloaded'
print 'It will be downloaded: '+info['title']

#Copio el link de descarga
clipboard.set(download_url)
console.hide_activity()
webbrowser.open('workflow://run-workflow?name=DownTube&input='+titulo)
