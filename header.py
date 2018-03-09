import re

header = str('1024\ndatabase_id -s5 TIMIT\ndatabase_version -s3 1.0\nutterance_id -s8 cjf0_sa1\nchannel_count -i 1\nsample_count -i 46797\nsample_rate -i 16000\nsample_min -i -2191\nsample_max -i 2790\nsample_n_bytes -i 2\nsample_byte_format -s2 01\nsample_sig_bits -i 16\nend_head\n\n\n\n\n')

#print(re.split(r'[sample_rate -i ]', '1024\ndatabase_id -s5 TIMIT\ndatabase_version -s3 1.0\nutterance_id -s8 cjf0_sa1\nchannel_count -i 1\nsample_count -i 46797\nsample_rate -i 16000\nsample_min -i -2191\nsample_max -i 2790\nsample_n_bytes -i 2\nsample_byte_format -s2 01\nsample_sig_bits -i 16\nend_head\n\n\n\n\n')


####print((re.search('(?<=sample_rate -i )\w+', header)).group(0))

#m = re.match(r"(?P<sample_rate -i >\w+)", header)
#m.group('sample_rate -i ')


#m = re.search("(?P<first_name>\w+) (?P<last_name>\w+)", "Joao Malcolm Reynolds")
#print(m.group('first_name'))


fs = (re.search('(?<=sample_rate -i )\w+', header)).group(0)
bits = (re.search('(?<=sample_sig_bits -i )\w+', header)).group(0)






if bits==16:
    signal = array.array('h', bytes_lidos[1024:])
    print(signal)
elif bits==8:
    signal = array.array('b', bytes_lidos[1024:])
    print(type(signal))


print(header)
