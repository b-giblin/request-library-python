filename = 'test.txt'
test_text = 'this is a test'

with open(filename, 'w') as f:
    f.write('hello\n')
    f.close()