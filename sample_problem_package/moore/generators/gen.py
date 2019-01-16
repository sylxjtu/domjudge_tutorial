import cyaron

example_datas = [1, 2]
secret_datas = list(range(3, 51))

for i in enumerate(example_datas):
    test_data = cyaron.IO(file_prefix="moore_example_", data_id=i[0], output_suffix=".ans")
    test_data.input_writeln(i[1])
    test_data.output_gen("std.exe")

for i in enumerate(secret_datas):
    test_data = cyaron.IO(file_prefix="moore_secret_", data_id=i[0], output_suffix=".ans")
    test_data.input_writeln(i[1])
    test_data.output_gen("std.exe")
