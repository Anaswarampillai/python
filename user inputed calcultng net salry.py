bs=int(input("enter the basic salary"))
if bs>=10000:
  da=bs*0.1
  hra=bs*0.15
  pf=bs*0.04
else:
    da=bs*0.2
    hra=bs*0.25
    pf=bs*0.06
    ns=bs+da+hra-pf
    print("basic salary :",bs)
    print("DA :",da)
    print("HRA :",hra)
    print("PF :",pf)
    print("net salary :",ns)
