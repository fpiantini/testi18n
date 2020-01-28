#!/usr/bin/env python
import gettext
import os
from trclass import TrClass

ldir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
print(f'Local dir is: {ldir}')
print(f'Default text domain is: {gettext.textdomain()}')
###print(gettext.bindtextdomain('messages', ldir))
###print(gettext.find('messages', ldir, ['it_IT'], True))
##print(gettext.find('messages', languages=['it_IT'], all=True))

t = gettext.translation('messages', ldir, fallback=True)
_ = t.gettext

lang_it = gettext.translation('messages', ldir, languages=['it_IT'], fallback=True)
lang_en = gettext.translation('messages', ldir, languages=['en_US'], fallback=True)

tc = TrClass()

print("----------------------------------------------")
print(' - DEFAULT LANG: -')
print(_('Hello world!'))
print(_('this is a translatable string'))
print(_('this is another string'))
tc.myprint()

# TO UNDERSTAND... da documentazione trovata online sembrerebbe
# che il cambio di linguaggio si possa fare anche tramite una
# chiamata al metodo install(): ma se si sostituisce la linea
# sotto con quella commentata non funziona
_ = lang_en.gettext
###lang_en.install()
print("----------------------------------------------")
print(' - en_US: -')
print(_('Hello world!'))
print(_('this is a translatable string'))
print(_('this is another string'))
tc.myprint()

_ = lang_it.gettext
###lang_it.install()
tc.setlang(lang_it)
print("----------------------------------------------")
print(' - it_IT: -')
print(_('Hello world!'))
print(_('this is a translatable string'))
print(_('this is another string'))
tc.myprint()


print("----------------------------------------------")

