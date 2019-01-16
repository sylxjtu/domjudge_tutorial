import cyaron

def randomBinaryString(n):
    return ''.join(str(cyaron.randint(0, 1)) for i in range(n))

example_datas = [
    ('1111', 3),
    ('11011', 6),
]

datas = []

for i in range(2): datas.append((randomBinaryString(cyaron.randint(1, 5)), cyaron.randint(0, 5)))
for i in range(2): datas.append((randomBinaryString(cyaron.randint(1, 10)), cyaron.randint(0, 10)))
for i in range(2): datas.append((randomBinaryString(cyaron.randint(1, 50)), cyaron.randint(0, 50)))
for i in range(6): datas.append((randomBinaryString(cyaron.randint(1, 100)), cyaron.randint(0, 100)))

datas += [
    ('1' * 100, 0),
    ('1' * 100, 1),    
    ('1' * 100, 100),
    ('0' * 100, 0),    
    ('0' * 100, 1),
    ('0' * 100, 100),
    ('01' * 50, 0),    
    ('01' * 50, 1),
    ('01' * 50, 2),
    ('1100' * 25, 0),
    ('1100' * 25, 1),
    ('1100' * 25, 2),
    ('1100' * 25, 3),
    ('1' * 50 + '0' + '1' * 49, 100),
    ('1' * 50 + '0' + '1' * 49, 49),
    ('1' * 50 + '0' + '1' * 49, 50),
    ('1' * 50 + '0' + '1' * 49, 0),    
]

for i in range(len(example_datas)):
    test_data = cyaron.IO(file_prefix="crack_example_", data_id=i, output_suffix=".ans")

    n = len(example_datas[i][0])
    m = example_datas[i][1]
    s = example_datas[i][0]
    test_data.input_writeln(n, m)
    test_data.input_writeln(s)

    test_data.output_gen("std.exe")

for i in range(len(datas)):
    test_data = cyaron.IO(file_prefix="crack_hidden_", data_id=i, output_suffix=".ans")

    n = len(datas[i][0])
    m = datas[i][1]
    s = datas[i][0]
    test_data.input_writeln(n, m)
    test_data.input_writeln(s)

    test_data.output_gen("std.exe")