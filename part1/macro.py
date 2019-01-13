######2016ucp1103
######macro_pre-processor

import re
code=open("code.asm","r")
expcode=open("expcode.asm","w")
deftab=open("deftab.txt","r+")
namtab=[]

set1=code.readlines()
len1=len(set1)

#############remove new lines
for i in range(len1):
    set1[i]=set1[i].strip('\n')
   # set1[i]=set1[i].strip('\t')

#############remove blank lines
j=0
while(j<len(set1)):
    if (not set1[j]):
        set1.pop(j)
        j=j-1
    j=j+1

#############creating namtab
count=0
k=0
for i in range(len(set1)):
    if "!!!M_START" in set1[i]:
        count=count+1
        if count==1:
            templist=[]
            p=set1[i].find("(")
            templist.append(set1[i][13:p-3])
            templist.append(i+1)
    elif "!!!M_FINISH" in set1[i]:
        count=count-1
        if count==0:
            templist.append(i+1)
            namtab.append(templist)
            k=k+1

##############creating deftab
for i in range(namtab[k-1][2]):
    set1[i]=set1[i]+'\n'
for i in range(namtab[k-1][2]):
    deftab.write(set1[i])

#############remove new line and tabs from macro portion in code file
for i in range(len(set1)):
    set1[i]=set1[i].strip('\n')
   # set1[i]=set1[i].strip('\t')

#############remove blank lines from macro portion in code file
j=0
while(j<len(set1)):
    if (not set1[j]):
        set1.pop(j)
        j=j-1
    j=j+1
#len1=len(set1)
#for i in range(len1):
#    print(set1[i])

################################function for argtab
def arg_fun(string,namtab,set1):
    y=string.find("..")
    z=string.find("(")
    macnam1=string[y+2:z-3]
    list2=[]
    list2.append(macnam1)
    if "!!!M_START" in string:                  #for nested macro
        arg1=[]
        arg2={}
        arg1=re.split('[,=]',string[z+1:len(string)-1])
        for m in range(0,len(arg1)-1,2):
            arg2[arg1[m]]=arg1[m+1]
        list2.append(arg2)

    else:                                       #for called macro
        arg1=[]
        arg1=re.split('[,]',string[z+1:len(string)-1])
        for m in range(len(arg1)):
            arg1[m]=str(arg1[m])
        for m in range(len(namtab)):
            if macnam1==namtab[m][0]:
                q=namtab[m][1]
        temp=set1[q-1]
        arg2={}
        y=temp.find("..")
        z=temp.find("(")
        arg3=re.split('[,=]',temp[z+1:len(temp)-1])
        e=1
        if arg1!=['']:
            for m in range(len(arg1)):
                arg3[e]=arg1[m]
                e=e+2
        for m in range(0,len(arg3)-1,2):
            arg2[arg3[m]]=str(arg3[m+1])
        list2.append(arg2)
 #   for t in range(len(list1)):
 #       if macnam1==list1[t][0]:
 #           list1[t]=list2
 #       else:
 #           list1.append(list2)
    return list2



################expanding code
def expand(x,y,macnam,argtab,namtab2,set1):
    c=1
    list1=[]
    list2=[]
    r=0
    dic={}
    dic=argtab[r][1]
    list1=list(dic.keys())
    list2=list(dic.values())

    while(c!=0 and x!=y):
        #if "***" in set1[x]:
        #    x=x+1
        #    continue
        if "!!!M_START" in set1[x]:
            r=r+1
            x=x+1
            c=c+1
            dic=argtab[r][1]
            list1=list(dic.keys())
            list2=list(dic.values())
            continue
        elif "!!!M_FINISH" in set1[x]:
            c=c-1
            x=x+1
        else:
			st=set1[x]
			if "<*" in set1[x]:
				z1=set1[x].find("<*")
				z2=set1[x].find("*>")
				st1=st[z1:z1+2]
				st=st.replace(st1,"")
            for n in range(0,len(list1)):
                if list1[n] in set1[x]:
                    st=st.replace(list1[n],list2[n])
            st=st+'\n'
            expcode.write(st)
            x=x+1

#############main algo
index=namtab[k-1][2]          ##start raeding from here
namtab2=namtab               #for nested macro names
nammacro=[]
name=[]
for x in range(len(namtab2)):
    nammacro.append(namtab[x][0])       #store only macro names
while(index<len(set1)):
    argtab=[]
    count1=0
    if "(" in set1[index]:                       #if there is a macro call
        count1=1
        a=set1[index].find("..")
        b=set1[index].find("(")
        macnam=set1[index][a+2:b-3]              #store macro name of called macro
        #print(macnam)
        for x in range(len(namtab2)):
            if macnam==namtab2[x][0]:             #macro is in namtab
                argt=arg_fun(set1[index],namtab2,set1)
                argtab.append(argt)
                p1=namtab2[x][1]
                p2=namtab2[x][2]
                while(count1!=0 and p1!=p2):     #count for nested macro
                    if "***" in set1[p1]:
                        pass
                    if "!!!M_START" in set1[p1]:
                        argt=arg_fun(set1[p1],namtab2,set1)
                        argtab.append(argt)
                        count1=count1+1
                        a=set1[p1].find("..")
                        b=set1[p1].find("(")
                        macnam=set1[p1][a+2:b-3]
                        if macnam in nammacro:
                            pass
                        else:
                            list1=[]
                            list1.append(macnam)
                            nammacro.append(macnam)
                            list1.append(p1+1)
                            count2=1
                            w=p1+1
                            while(count2!=0):
                                if "!!!M_START" in set1[w]:
                                    count2=count2+1
                                elif "!!!M_FINISH" in set1[w]:
                                    count2=count2-1
                                w=w+1
                            list1.append(w)
                            namtab2.append(list1)
                    elif "!!!M_FINISH" in set1[p1]:
                        count1=count1-1
                    p1=p1+1
                expand(namtab2[x][1],namtab2[x][2],namtab2[x][0],argtab,namtab2,set1)
            else:
                pass
        index=index+1
    else:                                        #if not macro call then write as it is in expcode
        set1[index]=set1[index]+'\n'
        expcode.write(set1[index])
        index=index+1
code.close()
expcode.close()
deftab.close()
