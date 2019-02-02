a = '<head>My new site</head>'
b = '<title>'
c = '</title>'

first = a.find(b)+len(b) if b and a.find(b) != -1 else 0
second = a.rfind(c) if c and a.rfind(c) != -1 else len(a)

res = a[first:second]
print(res)