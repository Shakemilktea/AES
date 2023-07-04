def SeparateKey(input_str):
    """
        Seperate String to List with step 2
        ex:
        input = '00112233445566778899aabbccddeeff'
        output = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
    :param input_str: String
    :return: List
    """
    return [input_str[i:i+2] for i in range(0, len(input_str), 2)]

def SubBytes(input_hex_str):
    """
        This STATE is given the fixed S-box value.
        IF YOU WANT TO MAKE YOUR OWN S-BOX, YOU NEED TO WRITE A NEW ALGORITHM TO GENERATE IT.
    :param input_hex_str: hex_str
    :return: hex_str
    """
    input_lst = SeparateKey(input_hex_str)
    S_BOX = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

    return ''.join([hex(S_BOX[int(i, 16)])[2:].zfill(2) for i in input_lst])

def ShiftRows(input_hex_str):
    """
        Change List to Matrix. And then ShiftRow.
        ex: (Matrix Example)
        [[0, 4, 8, 12],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15]]
    :param input_hex_str: hex_str
    :return: hex_str
    """
    input_lst = SeparateKey(input_hex_str)
    # Change the List to Matrix
    row_len = len(input_lst) // 4
    matrix = [list(column) for column in zip(*[input_lst[i:i+row_len] for i in range(0, len(input_lst), row_len)])]

    # ShiftRow
    if row_len == 8:
        matrix[1] = matrix[1][1:] + matrix[1][:1]
        matrix[2] = matrix[2][3:] + matrix[2][:3]
        matrix[3] = matrix[3][4:] + matrix[3][:4]
    else:
        for i in range(4):
            matrix[i] = matrix[i][i:] + matrix[i][:i]
    # change back to List
    return ''.join([matrix[j][i] for i in range(len(matrix[0])) for j in range(4)])

def MixColumns(input_hex_str):
    """
        MixColumns values.
    :param input_hex_str: hex_str
    :return: hex_str
    """
    input_lst = SeparateKey(input_hex_str)
    input_lst = [input_lst[i:i+4] for i in range(0, len(input_lst), 4)]
    matrix = [[0x02, 0x03, 0x01, 0x01],
              [0x01, 0x02, 0x03, 0x01],
              [0x01, 0x01, 0x02, 0x03],
              [0x03, 0x01, 0x01, 0x02]]

    output = [['00' for i in range(4)] for j in range(len(input_lst))]
    for row in range(4):
        for column in range(len(input_lst[0])):
            for k in range(4):
                if matrix[row][k] == 3:
                    output[row][column] = XOR(XOR(xtime(input_lst[column][k]), input_lst[column][k]), output[row][column])
                elif matrix[row][k] == 2:
                    output[row][column] = XOR(xtime(input_lst[column][k]), output[row][column])
                else:
                    output[row][column] = XOR(input_lst[column][k], output[row][column])

    # change back to List
    return ''.join([output[j][i] for i in range(len(output[0])) for j in range(4)])

def AddRoundKey(input_lst, roundkey):
    """
        Add cipher text & roundkey
    :param input_lst: List
    :param roundkey: String
    :return: String
    """
    return XOR(''.join(input_lst), roundkey)

def InvMixColumns(input_hex_str):
    """
    :param input_hex_str: hex_str
    :return: hex_str
    """
    input_lst = SeparateKey(input_hex_str)
    input_lst = [input_lst[i:i + 4] for i in range(0, len(input_lst), 4)]
    matrix = [[0x0e, 0x0b, 0x0d, 0x09],
              [0x09, 0x0e, 0x0b, 0x0d],
              [0x0d, 0x09, 0x0e, 0x0b],
              [0x0b, 0x0d, 0x09, 0x0e]]

    output = [['00' for i in range(4)] for j in range(len(input_lst))]
    for row in range(4):
        for column in range(len(input_lst[0])):
            for k in range(4):
                if matrix[row][k] == 14:
                    output[row][column] = XOR(XOR(XOR(xtime(xtime(xtime(input_lst[column][k]))),    # x^3
                                                      xtime(xtime(input_lst[column][k]))),          # x^2
                                                  xtime(input_lst[column][k])),                     # x^1
                                              output[row][column])
                elif matrix[row][k] == 11:
                    output[row][column] = XOR(XOR(XOR(xtime(xtime(xtime(input_lst[column][k]))),    # x^3
                                                      xtime(input_lst[column][k])),                 # x^1
                                                  input_lst[column][k]),                            # x^0
                                              output[row][column])
                elif matrix[row][k] == 13:
                    output[row][column] = XOR(XOR(XOR(xtime(xtime(xtime(input_lst[column][k]))),    # x^3
                                                      xtime(xtime(input_lst[column][k]))),          # x^2
                                                  input_lst[column][k]),                            # x^0
                                              output[row][column])
                else:   # matrix[row][k] == 9
                    output[row][column] = XOR(XOR(xtime(xtime(xtime(input_lst[column][k]))),        # x^3
                                                  input_lst[column][k]),                            # x^0
                                              output[row][column])

    # change back to List
    return ''.join([output[j][i] for i in range(len(output[0])) for j in range(4)])

def InvShiftRows(input_hex_str):
    """
    :param input_hex_str: hex_str
    :return: hex_str
    """
    input_lst = SeparateKey(input_hex_str)
    # Change the List to Matrix
    row_len = len(input_lst) // 4
    matrix = [list(column) for column in zip(*[input_lst[i:i + row_len] for i in range(0, len(input_lst), row_len)])]

    # ShiftRow
    if row_len == 8:
        matrix[1] = matrix[1][-1:] + matrix[1][:-1]
        matrix[2] = matrix[2][-3:] + matrix[2][:-3]
        matrix[3] = matrix[3][-4:] + matrix[3][:-4]
    else:
        for i in range(4):
            matrix[i] = matrix[i][-i:] + matrix[i][:-i]
    # change back to List
    return ''.join([matrix[j][i] for i in range(len(matrix[0])) for j in range(4)])

def InvSubBytes(input_hex_str):
    """
    :param input_hex_str: hex_str
    :return: hex_str
    """
    input_lst = SeparateKey(input_hex_str)
    S_BOX = ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb',
             '7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb',
             '54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e',
             '08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25',
             '72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92',
             '6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84',
             '90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06',
             'd0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b',
             '3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73',
             '96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e',
             '47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b',
             'fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4',
             '1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f',
             '60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef',
             'a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61',
             '17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']

    return ''.join([S_BOX[int(i, 16)] for i in input_lst])


def KeyExpansion(key, Nr):
    """
    :param key: str_hex
    :param Nr: int
    :return: List
    """

    key = [key[i:i + 8] for i in range(0, len(key), 8)]
    Nk = len(key)
    if Nk == 4 or Nk == 6:
        for i in range(Nk, Nk * (Nr + 1)):
            if (i % Nk) == 0:
                temp = key[-1]
                temp = temp[2:] + temp[:2]
                temp = XOR(XOR(SubBytes(temp), Rcon(i // Nk)),
                           ''.join([key[-Nk][i:i + 2] for i in range(0, len(key[-Nk]), 2)]))
            else:
                temp = XOR(key[-1], key[-Nk])
            key.append(temp)
    elif Nk == 8:
        for i in range(Nk, Nk * (Nr + 1)):
            if (i % Nk) == 0 and (i % 4) == 0:
                temp = key[-1]
                temp = temp[2:] + temp[:2]
                temp = XOR(XOR(SubBytes(temp), Rcon(i // Nk)),
                           ''.join([key[-Nk][i:i + 2] for i in range(0, len(key[-Nk]), 2)]))
            elif (i % Nk) != 0 and (i % 4) == 0:
                temp = XOR(SubBytes(key[-1]), key[-Nk])
            else:
                temp = XOR(key[-1], key[-Nk])
            key.append(temp)

    return [''.join(key[i:i+4]) for i in range(0, len(key), 4)]

def XOR(hex1, hex2):
    """
        Just XOR.
    :param hex1: string
    :param hex2: string
    :return: string
    """

    if len(hex1) == len(hex2):
        max_len = len(hex1) * 4

        # 去掉前面0b的部分，轉換成二進位
        bin1 = bin(int(hex1, 16))[2:]
        bin2 = bin(int(hex2, 16))[2:]

        # 根據長度填充往前填充0
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        # 進行XOR運算
        result_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(bin1, bin2))

        # 轉回16進位
        return hex(int(result_bin, 2))[2:].zfill((max_len + 3) // 4)
    else:
        print("Input and Cipher Key are different lengths")
        return 0

def xtime(hex0):
    """
        Left shift. If the first number is 1, then XOR '1b'
    :param hex0: str_hex
    :return: str_hex
    """
    bin0 = bin(int(hex0, 16))[2:].zfill(8)
    if bin0[0] == '1':
        # left shift
        bin0 = bin0[1:]+'0'
        # XOR
        result_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(bin0, '00011011'))
        # change back to hex
        return hex(int(result_bin, 2))[2:].zfill(2)
    else:
        # left shift
        result_bin = bin0[1:]+'0'
        # change back to hex
        return hex(int(result_bin, 2))[2:].zfill(2)

def Rcon(j):
    """
    :param j: int
    :return: String
    """
    temp = '01'
    for i in range(j - 1):
        temp = xtime(temp)
    return temp+'000000'