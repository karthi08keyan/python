
filename1 = open ('Downloads/da/output.txt','r')
import re
strValue= filename1.read()
ch = '<!DOCTYPE html>'
# patern = ".*" + ch
before,sep,after = strValue.partition(ch)
if len (after) > 0:
    strValue = after
    # print(strValue)
# strValue = re.sub(patern, '',strValue)
# print(strValue)
css_script = re.compile('<\s*style[^>]*>.*?<\s*/\s*style\s*>',re.S | re.I)
strValue = css_script.sub('',strValue)
html = re.compile(r'<[^>]+>',re.S | re.I)
specl_char = re.compile(r'/')
strValue = specl_char.sub('',strValue)
strValue = html.sub('',strValue)
result = re.sub(' +','',strValue)
result = " ".join(strValue.split())
print("Message:",result)
