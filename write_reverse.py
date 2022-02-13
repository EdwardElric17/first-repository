mas_read = []
mas_write = []
with open('dataset_24465_4.txt', 'r') as inf:
    for line in inf:
        mas_read.append(line.rstrip())
mas_write = [str(i) for i in mas_read[::-1]]
with open('test.txt', 'w') as ouf:
    for line in mas_write:
        ouf.write(line + '\n')