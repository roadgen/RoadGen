from func.printAuto import printAutoInd


def printConnection(widgetA, widgetB, type, f):
    printAutoInd(f, '% Combine widgets')
    if type == '单行道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        print('组件拼接完成')
    elif type == '单向虚线双行道' or type == '单向实线双行道' or type == '单向虚实线双行道' or type == '单向双实线双行道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                1]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                1]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[1]) + '"));')
        print('组件拼接完成')
    elif type == '双向虚线双行道' or type == '双向实线双行道' or type == '双向虚实线双行道' or type == '双向双实线双行道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                1]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                1]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[1]) + '"));')
        print('组件拼接完成')
    elif type == '一前行虚白线虚黄线三行道' or type == '一前行实白线虚黄线三行道' or type == '一前行虚白线实黄线三行道' or type == '一前行实白线实黄线三行道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                1]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                1]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                2]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[2]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                2]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[2]) + '"));')
        print('组件拼接完成')
    elif type == '二前行虚黄线虚白线三行道' or type == '二前行虚黄线实白线三行道' or type == '二前行实黄线虚白线三行道' or type == '二前行实黄线实白线三行道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                1]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                1]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                2]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[2]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                2]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[2]) + '"));')
        print('组件拼接完成')
    elif type == '双黄实线虚虚四车道' or type == '双黄实线实实四车道' or type == '双黄实线虚实四车道' or type == '双黄实线实虚四车道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                1]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                1]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                2]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[2]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                2]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[2]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                3]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[3]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                3]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[3]) + '"));')
        print('组件拼接完成')
    elif type == '双实线虚虚虚虚六车道' or type == '双实线实实实实六车道' or type == '双实线虚虚实实六车道':
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[0]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                1]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                1]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[1]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                2]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[2]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                2]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[2]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                3]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[3]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                3]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[3]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                4]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[4]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                4]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[4]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetA[
                5]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetB[5]) + '"));')
        printAutoInd(f, 'rrMap.Lanes(' + str(
            widgetB[
                5]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
            widgetA[5]) + '"));')
        print('组件连接拼接完成')

    return
