string=str(input())
def check_brackets(string):
    brackets_open=('(', '[', '{')
    brackets_close=(')', ']', '}')
    stack=list()
    opened=list()
    counter=0
    for i in string:
        counter +=1
        if i in brackets_open:
            stack.append(i)
            opened.append(counter)
        elif i in brackets_close:
            if len(stack) == 0:
                return counter
            index_close=brackets_close.index(i)
            open_bracket=brackets_open[index_close]
            top=stack.pop()
            if (top !=open_bracket):
                return counter
            else:
                opened.pop()
    if len(stack) == 0:
        return "Success"
    else:
        return opened.pop()
    
print(check_brackets(string))