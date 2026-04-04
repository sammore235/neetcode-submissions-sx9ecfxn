class Solution:
    def isValid(self, s: str) -> bool:
        stringlist = list(s)
        count = 0
        test = ['}',')',']']
        if len(stringlist)%2!=0:
            return False
        elif stringlist[0] in test:
            return False
        repeat = int(len(stringlist)/2)

        for i in range(0,repeat):
            print(stringlist,i)
            if stringlist[0]=="(":
                if stringlist[-1]==")":
                    stringlist.pop(0)
                    stringlist.pop(-1)
                    continue
                elif stringlist[1]==")":
                    stringlist.pop(0)
                    stringlist.pop(0)
                    continue
                else:
                    return False
            elif stringlist[0]=="{" :
                if stringlist[-1]=="}":
                    stringlist.pop(0)
                    stringlist.pop(-1)
                    continue
                elif stringlist[1]=="}":
                    stringlist.pop(0)
                    stringlist.pop(0)
                    continue
                else:
                    return False
            elif stringlist[0]=="[" :
                if stringlist[-1]=="]":
                    stringlist.pop(0)
                    stringlist.pop(-1)
                    continue
                elif stringlist[1]=="]":
                    stringlist.pop(0)
                    stringlist.pop(0)
                    continue
                else:
                    return False
            else:
                return False
        return True
  