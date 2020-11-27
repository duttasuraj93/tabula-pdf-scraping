import tabula

file = "test.pdf"
table = tabula.read_pdf(file, guess=False, pages='63', output_format='json')

data = []
for i, value in table[0].items():  
    if i == 'data':
        data = value

data = data[2:]
data = data[:len(data)-5]

for i in data:
    print(i[0])