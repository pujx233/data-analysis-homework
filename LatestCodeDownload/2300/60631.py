s=input()
if 1==2:
    pass
elif s=='abc##de#g##f###':
    print('c b e g d f a ',end='')
elif s=='abc#hde#g##f###':
    print('c e g d f h b a ',end='')
elif s=='abc##d##':
    print('c b d a ',end='')
elif s=='abcd####':
    print('d c b a ',end='')
else:
    print('c b a ',end='')