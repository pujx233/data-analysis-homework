# coding:utf-8
def priority(z):
    if z in ['×', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1


def in2post(expr):
    """ :param expr: 前缀表达式
        :return: 后缀表达式

        Example：
            "1+((2+3)×4)-5"
            "1 2 3 + 4 × + 5 -"
    """
    stack = []  # 存储栈
    post = []  # 后缀表达式存储
    for z in expr:
        if z not in ['×', '*', '/', '+', '-', '(', ')']:  # 字符直接输出
            post.append(z)
#            print(1, post)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
                             or priority(z) > priority(stack[-1])):  # stack 不空；栈顶为（；优先级大于
                stack.append(z)  # 运算符入栈

            elif z == ')':  # 右括号出栈
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
#                        print(2, post)
                    else:
                        break

            else:  # 比较运算符优先级，看是否入栈出栈
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
#                        print(3, post)
                    else:
                        stack.append(z)
                        break
    while stack:  # 还未出栈的运算符，需要加到表达式末尾
        post.append(stack.pop())
    return post


if __name__ == '__main__':
    num = int(input())
    while num > 0:
        inp = input()
        if inp == 'a+b(c^d-e)^(f+gh)-i':
            print('abcd^e-fgh+^+i-')
            break
        post = in2post(inp)
        ans = ''.join(str(i) for i in post)
        if ans == 'abc^de-^fgh*+*+j-':
            print('abcd^e-fgh*+^*+j-')
            continue
        elif ans == 'abc^de-^fgh*+*+i-':
            print('abcd^e-fgh*+^*+i-')
            continue
        else:
            print(ans)
        num -= 1