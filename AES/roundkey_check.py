import library

def write_to_txt_file(text, file_name):
    with open(file_name, 'a') as f:
        f.write(text)

key = '00112233445566778899aabbccddeeff'
file_name = 'roundkey_check.txt'
counter = 0

roundkey = library.KeyExpansion(key, 10)
roundkey_lst = ''.join(roundkey)
print(roundkey_lst)
write_to_txt_file(roundkey_lst, file_name)
counter += len(roundkey_lst)

for i in range(312500): #312500
    roundkey = library.KeyExpansion(roundkey[-1], 10)
    roundkey_lst = ''.join(roundkey[1:])
    print(roundkey_lst)
    write_to_txt_file(roundkey_lst, file_name)
    counter += len(roundkey_lst)
print("TOTAL length:", counter)
