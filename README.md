Python Unicode/XCompose Generator
===================================

Some handy unicode tables and a script to generate XCompose files. I wrote it a while back and it may be useful for someone.

The tables, present, are:

 * greek
 * superscripts
 * superscripts_greek
 * subscripts
 * subscripts_greek
 * double_struck
 * double_struck_greek
 * mathematical_italic
 * mathematical_script
 * texsymb

The XCompose script is inspired by [Kragen's work](https://github.com/kragen/xcompose). My script automates repetitive content in the XCompose file, for example:

```python
for ascii, symb, tex in greek:
	if ascii != "": 
		f.addline("*" + ascii, symb, comment = tex)
``` 

Instead of:

```
<Multi_key> <asterisk> <a>              : "α"   U03B1           # GREEK SMALL LETTER ALPHA
<Multi_key> <asterisk> <b>              : "β"   U03B2           # GREEK SMALL LETTER BETA
...

```

This makes it much easier to customize your XCompose.

Syntactically, the script is also much nicer. For example:

```python
f.addline(u"→→",  u"→")
f.addline(u"←←",  u"←")
...
f.addline("<=", u"≤")
f.addline(">=", u"≥")
...
```

Compared to:

```
Multi_key> <Left> <Left>               : "←"   leftarrow       # LEFTWARDS ARROW
<Multi_key> <Up> <Up>                   : "↑"   uparrow         # UPWARDS ARROW
...
<Multi_key> <less> <equal>              : "≤"   U2264           # LESS-THAN OR EQUAL TO
<Multi_key> <greater> <equal>           : "≥"   U2265           # GREATER-THAN OR EQUAL TO
...
```


