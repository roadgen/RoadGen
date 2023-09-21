# 实现matlab代码的自动缩进的问题
cIndents = 0
isPreLineSwitch = 0
isDummyPrint = False

def printAutoInd(f, inputStr, *argins):
    global cIndents, isPreLineSwitch, isDummyPrint

    if isDummyPrint:
        # Do nothing
        return

    if isinstance(f, list):
        f.append(inputStr.format(*argins))
        return

    incrAfterStr = ('if', 'try', 'switch', 'for', 'while', 'properties', 'methods', 'classdef')
    decreAndIncrStr = ('else', 'elseif', 'otherwise', 'catch')

    keyWordStr = inputStr.split(' ')[0]

    if keyWordStr in incrAfterStr:
        tabStrs = '\t' * cIndents

        print(f"{tabStrs}{inputStr}".format(*argins), file=f)
        # print(f"\n{tabStrs}{inputStr}".format(*argins), file=f)

        cIndents += 1

    elif keyWordStr in decreAndIncrStr:
        cIndents -= 1
        tabStrs = '\t' * cIndents

        print(f"{tabStrs}{inputStr}".format(*argins), file=f)

        cIndents += 1

    elif 'end' == keyWordStr:
        cIndents -= 1
        tabStrs = '\t' * cIndents

        print(f"{tabStrs}{inputStr}".format(*argins), file=f)
        # print(f"{tabStrs}{inputStr}\n".format(*argins), file=f)

    elif 'end%switch' == keyWordStr:
        cIndents -= 2
        tabStrs = '\t' * cIndents

        print(f"{tabStrs}{inputStr}".format(*argins), file=f)
        # print(f"{tabStrs}{inputStr}\n".format(*argins), file=f)

    elif 'case' == keyWordStr:

        if 0 == isPreLineSwitch:
            cIndents -= 1

        tabStrs = '\t' * cIndents

        print(f"{tabStrs}{inputStr}".format(*argins), file=f)

        cIndents += 1

    else:

        tabStrs = '\t' * cIndents

        print(f"{tabStrs}{inputStr}".format(*argins), file=f)

    if 'switch' == keyWordStr:
        isPreLineSwitch = 1
    else:
        isPreLineSwitch = 0

    if cIndents < 0:
        cIndents = 0

    return