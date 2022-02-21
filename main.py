msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [None, None, None, None, None, None,
        None, None, None, None, msg_10, msg_11, msg_12]


def is_one_digit(v):
    v = float(v)
    return v > -10 and v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


memory = 0

flag_2 = True

flag_1 = True

flag_3 = True

flag_4 = True

while flag_1:
    flag_2 = True
    flag_3 = True
    flag_4 = True
    print(msg_0)
    res = 0
    try:
        calc = input()
        x, oper, y = calc.split()
        if x == 'M':
            x = memory
        if y == 'M' and x != 'M':
            y = memory
        if not str(x).replace('.', '', 1).isdigit() or not str(y).replace('.', '', 1).isdigit():
            print(msg_1)
        else:
            if oper in ['+', '-', '*', '/']:
                x = float(x)
                y = float(y)
                check(v1=x, v2=y, v3=oper)
                if oper == '+':
                    res = x + y
                elif oper == '-':
                    res = x - y
                elif oper == '*':
                    res = x * y
                elif oper == '/' and y != 0:
                    res = x / y
                elif oper == '/' and y == 0:
                    print(msg_3)
                    continue
            else:
                print(msg_2)
                continue
    except ValueError:
        print(msg_1)
    else:
        flag_1 = False
        print(res)
        while flag_2:
            print(msg_4)
            answer = input()
            if answer.lower() == 'y':
                if is_one_digit(res):
                    msg_index = 10
                    while flag_4:
                        print(msg_[msg_index])
                        answer_3 = input()
                        if answer_3.lower() == 'y':
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                memory = res
                                flag_4 = False
                        elif answer_3.lower() == 'n':
                            flag_4 = False
                        else:
                            continue
                else:
                    memory = res
            elif answer.lower() == 'n':
                pass
            else:
                continue
            while flag_3:
                print(msg_5)
                answer_2 = input()
                if answer_2.lower() == 'y':
                    flag_1 = True
                    flag_2 = False
                    flag_3 = False
                elif answer_2.lower() == 'n':
                    flag_1 = False
                    flag_2 = False
                    flag_3 = False
                else:
                    continue
