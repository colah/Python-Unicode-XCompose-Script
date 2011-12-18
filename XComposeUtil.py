# coding=UTF-8

import codecs
from math import ceil

def XCompose_line(s,c,comment=""):
	def uform(c):
		def capitalize_all(s):
			if len(s) > 1: return s[0].capitalize() + capitalize_all(s[1:])
			return s[0].capitalize()
		if len(c) == 1:
			return "U"+capitalize_all(hex(ord(c))[2:])
		else:
			return ""
	def rule(s):
		swaps = {">" : "greater",
		         "<" : "less",
		         "(" : "parenleft",
		         ")" : "parenright",
		         "[" : "bracketleft",
		         "]" : "bracketright",
		         "{" : "braceleft",
		         "}" : "braceright",
		         "@" : "at",
		         "#" : "numbersign",
		         #"$" : "", ????
		         "%" : "percent",
		         "^" : "asciicircum",
		         "&" : "ampersand",
		         "*" : "asterisk",
		         "_" : "underscore",
		         " " : "space",
		         "-" : "minus", 
		         "+" : "plus",
		         "=" : "equal",
		         "?" : "question",
		         "." : "period",
		         "|" : "bar",
		         "/" : "slash",
		         "~" : "asciitilde",
		         "\\" : "backslash",
		         u"→" : "right", 
		         u"←" : "left", 
		         u"↑" : "up", 
		         u"↓" : "down"     
		}
		ret="<Multi_key>"
		for c in s:
			if c in swaps.keys():
				ret += " <" + swaps[c] + ">"
			else:
				ret += " <" + c +">"
		return ret
	print comment
	r = rule(s)
	test = " ".join(map(lambda s: s.ljust(12), r.split(' ')[:-1])+[r.split(' ')[-1]])
	if len(test) <= 46:
		r = test.ljust(46)
	else:
		r = r.ljust(max(46, int(ceil(len(r)/10)*10))) 
	return r + " : " + ("\"" + c +"\" " + uform(c)).ljust(10) + " # " + comment


class XComposeFile:
	def __init__(self, name):
		self.f = codecs.open(name, encoding='utf-8', mode='w')
	def addline(self, s,c,comment=""):
		self.f.write(XCompose_line(s, c, comment)+"\n")
	def close(self):
		self.f.write(XCompose_line(s, c, comment)+"\n")


