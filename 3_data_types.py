def wordcount(fname):
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened')
        exit()

    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

    return count

f_1      = './data/test_file_1.txt'
count    = wordcount(f_1)
filtered = { key:value for key, value in count.items() if value > 5 and value < 20 }

print(filtered)
