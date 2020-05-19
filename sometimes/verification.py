# 八个字符校验至少包含一个数据，含有大小写字母
import re,pyperclip
verifRegex=re.compile('''([A-Z]+ |[a-z]+ |/d +){8,}''')
text=pyperclip.paste()
text=str(pyperclip.paste())
matches=[]
print(verifRegex.findall(text))
for group in verifRegex.findall(text):
    matches.append(group[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('匹配失败')