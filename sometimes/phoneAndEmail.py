# 匹配搜索电话和邮件
import re,pyperclip
# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))? #地区号
# (\s|-|\.)?
# (\d{3})             #中间三位数字
# (\s|-|\.)
# (\d{4})             #后边四位
# (\s*(ext|x|ext\.)\s(\d{2,5}))?
# )''',re.VERBOSE)
phoneRegex = re.compile(r'''(
1[3-9]
([0-9]{9})
)''',re.VERBOSE)
EmailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #用户
@        
[a-zA-Z0-9]+            #
(\.[a-zA-z]{2,4})
)''',re.VERBOSE)
text=str(pyperclip.paste())
matches=[]
print(phoneRegex.findall(text))
for group in phoneRegex.findall(text):
    # phoneNum='-'.join([group[1],group[3],group[5]])
    # if group[8]=='':
    #     phoneNum+=' x'+group[8]
    # matches.append(phoneNum)
    matches.append(group[0])
for group in EmailRegex.findall(text):
    matches.append(group[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('没有匹配到电话或者邮箱')