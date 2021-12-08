nmsp_var = {'global':set()}
prnt_nmsp = {'None':'global'}
for i in input():
    cmd, namespace, var = (str(j) for j in input().split())
    if cmd == 'create':
        if var not in prnt_nmsp:
            prnt_nmsp[var] = set()
        prnt_nmsp[var].append(namespace)
    if cmd == 'add':
        if var not in nmsp_var:
            nmsp_var[namespace] = set()
        nmsp_var[namespace].append(var)
    if cmd == 'get':
        if var in nmsp_var[namespace]:
            print(namespace)
        elif var not in nmsp_var[namespace]:
            def get_key(var):
                for key, value in prnt_nmsp.items():
                    if namespace == value:
                        if var in nmsp_var[namespace]:
                            return(key)
                        else:
                            k = key
                            get_key(k)