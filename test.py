nmsp_var = {'global':[]} 
prnt_nmsp = {'None':['global']} 
for i in range(int(input())):
    cmd, namespace, var = (str(j) for j in input().split()) 
    if cmd == 'create':
        if var not in prnt_nmsp:
            prnt_nmsp[var] = []
            nmsp_var[namespace] = []
        if namespace not in nmsp_var:
            nmsp_var[namespace] = []
        prnt_nmsp[var].append(namespace) 
    if cmd == 'add': 
        if namespace not in nmsp_var:  
            nmsp_var[namespace] = []
        nmsp_var[namespace].append(var) 
print(prnt_nmsp)
print(nmsp_var)