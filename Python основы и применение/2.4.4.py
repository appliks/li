with open('C:/Users/li/Downloads/dataset_24465_4.txt') as f1:
    f1_lines = f1.read().splitlines()

with open('C:/Users/li/Downloads/result.txt', 'w') as f2:
    for line in f1_lines[::-1]:
        f2.write('%s\n' % line)