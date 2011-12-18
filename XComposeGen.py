# coding=UTF-8

# Inspired by https://github.com/kragen/xcompose
# I wanted to make an easier to modify XCompose file. 
# Repetitive stuff can be handeled by loops.
# Much easier format.

import codecs
from tables import *
from XComposeUtil import XComposeFile

f = XComposeFile("XComposeTest")

#f.addline(<Keys to bind to>, <symbol> (optional:, <comment>) )
# Arrows represent the arrow keys.

f.addline(u"→→",  u"→")
f.addline(u"←←",  u"←")
f.addline(u"↑↑",  u"↑")
f.addline(u"↓↓",  u"↓")
f.addline(u"↓←",  u"↵")
f.addline(u"←→",  u"↔")
f.addline(u"↑↓",  u"↕")
f.addline(u"=→→", u"⇒")
f.addline(u"=←←", u"⇐")
f.addline(u"=↑↑", u"⇑")
f.addline(u"=↓↓", u"⇓")
f.addline(u"=←→", u"⇔")
f.addline(u"=↑↓", u"⇕")

f.addline(">=", u"≥")
f.addline("<=", u"≤")
f.addline("~=", u"≅")
f.addline("/=", u"≠")
f.addline("=?", u"≟")
f.addline("==", u"≡")

f.addline("+-", u"±")
f.addline("-+", u"∓")



for ascii, symb, tex in superscripts:
	if ascii != "": 
		f.addline("^" + ascii, symb, comment = "sup " + ascii)

for ascii, symb, tex in subscripts:
	if ascii != "": 
		f.addline("_" + ascii, symb, comment = "sub " + ascii)

for ascii, symb, tex in greek:
	if ascii != "": 
		f.addline("*" + ascii, symb, comment = tex)

for ascii, symb, tex in superscripts_greek:
	if ascii != "": 
		f.addline("^*" + ascii, symb, comment = "sup " + tex[1:])

for ascii, symb, tex in subscripts_greek:
	if ascii != "": 
		f.addline("_*" + ascii, symb, comment = "sub " + tex[1:])

for ascii, symb, tex in double_struck:
	if ascii != "": 
		f.addline("|" + ascii, symb, comment = "double struck " + ascii)

for ascii, symb, tex in mathematical_script:
	if ascii != "": 
		f.addline("%" + ascii, symb, comment = "math script " + ascii)

for ascii, symb, tex in mathematical_italic:
	if ascii != "": 
		f.addline("$" + ascii, symb, comment = "math italic " + ascii)

for _, symb, tex in texsymb:
	f.addline("\\" + tex + "\\", symb, comment = "LaTeX: " + tex)

