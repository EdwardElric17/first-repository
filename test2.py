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
    if cmd == 'get': 
        if var in nmsp_var[namespace]: 
            print(namespace)
            continue
        elif namespace == 'global':
            print('None')
            continue
        else:            
            def get_key(namespace): 
                for key, value in prnt_nmsp.items(): 
                    if namespace in value: 
                        if var in nmsp_var[key]: 
                            print(key) 
                            break
                        else:
                            if key == 'global':
                                print('None')
                            else:    
                                k = key
                                get_key(k)
        get_key(namespace)