end = False
funclist = ['def', 'calc', 'see']
calclist = ['+', '-', '/', '*', '=']
vardict = {}
while not end:
    invalidcommanderror = False
    name = input()
    func = name.split(' ')[0]
    if func.lower() == 'quit':
        end = True
        break
    if func not in funclist:
        print('undefined')
    if func == 'def':
        if name.count('=') != 1:
            print('ERROR: INVALID COMMAND')
        else:
            equal = name.index('=')
            var = name[3:equal].strip()
            if var == '':
                invalidcommanderror = True
            for t in var:
                if t in calclist:
                    invalidcommanderror = True
            if var.isnumeric():
                invalidcommanderror = True
            val = name[equal+1:].strip()
            if val != '' and val.isnumeric():
                if float(val).is_integer():
                    val = int(float(val))
            else:
                invalidcommanderror = True
            if invalidcommanderror:
                print('ERROR: INVALID COMMAND')
            else:
                vardict[var] = val
    if func == 'calc':
        test = 0
        for t in name:
            if t in calclist:
                test += 1
        if test != 1:
            print('ERROR: INVALID COMMAND')
        else:
            operator = 0
            for t in name:
                if t in calclist:
                    operator = name.index(t)
            frontvar = name[4:operator].strip()
            backvar = name[operator + 1:].strip()
            if frontvar == '' or backvar == '':
                print('ERROR: INVALID COMMAND')
            else:
                vartest = True
                if not frontvar.isnumeric():
                    if frontvar not in vardict:
                        vartest = False
                    else:
                        frontvar = vardict[frontvar]
                else:
                    frontvar = int(float(frontvar))
                if not backvar.isnumeric():
                    if backvar not in vardict:
                        vartest = False
                    else:
                        backvar = vardict[backvar]
                else:
                    backvar = int(float(backvar))
                if not vartest:
                    print('ERROR: VARIABLE IS NOT DEFINED')
                else:
                    if name[operator] == '/':
                        if backvar == 0:
                            print('ERROR: DIVISION BY ZERO')
                        else:
                            if (frontvar / backvar).is_integer():
                                print(int(frontvar / backvar))
                            else:
                                print(format((frontvar / backvar), ".3f"))
                    elif name[operator] == '+':
                        print(frontvar + backvar)
                    elif name[operator] == '-':
                        print(frontvar - backvar)
                    elif name[operator] == '*':
                        print(frontvar * backvar)

    if func == 'see':
        print('======Variables======')
        for t in vardict.keys():
            print(t, ':', vardict[t])
