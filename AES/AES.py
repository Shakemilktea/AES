import library

if __name__ == '__main__':
    """
        NOW, THE MESSAGE LENGTH ONLY CAN BE 32. NEED TO UPGRADE THE CODE.
    """
    message = '00112233445566778899aabbccddeeff'
    key = '000102030405060708090a0b0c0d0e0f'
    # key = '000102030405060708090a0b0c0d0e0f1011121314151617'
    # key = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'

    # message = '3243f6a8885a308d313198a2e0370734'
    # key = '2b7e151628aed2a6abf7158809cf4f3c'
    # key = '8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b'
    # key = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'

    # EASY CODING, KEY LENGTH SHOULD BE (32, 48 ,64).
    if len(message) == 32 and len(key) == 32:
        Nr = 10
    elif len(message) == 64 or len(key) == 64:
        Nr = 14
    else:
        Nr = 12
    print('Number of round:', Nr)

    roundkey = library.KeyExpansion(key, Nr)
    print(roundkey)

    # START Encrypt
    print('Encrypt')
    print('round[0].input', message)
    print('round[0].k_sch', roundkey[0])
    STATE0 = library.XOR(message, roundkey[0])  # the STATE0 here is a string, need to change to List (TO BE A MATRIX)
    counter = 1
    for i in range(1, Nr):
        print(f'round[{counter}].start', STATE0)
        STATE1 = library.SubBytes(STATE0)
        print(f'round[{counter}].s_box', STATE1)
        STATE2 = library.ShiftRows(STATE1)
        print(f'round[{counter}].s_row', STATE2)
        STATE3 = library.MixColumns(STATE2)
        print(f'round[{counter}].m_col', STATE3)
        print(f'round[{counter}].k_sch', roundkey[i])
        STATE0 = library.AddRoundKey(STATE3, roundkey[i])
        counter += 1
    print(f'round[{counter}].start', STATE0)
    STATE1 = library.SubBytes(STATE0)
    print(f'round[{counter}].s_box', STATE1)
    STATE2 = library.ShiftRows(STATE1)
    print(f'round[{counter}].s_row', STATE2)
    print(f'round[{counter}].k_sch', roundkey[Nr])
    STATE0 = library.AddRoundKey(STATE2, roundkey[Nr])
    print(f'round[{counter}].output', STATE0)


    # START Decrypt (EQUIVALENT INVERSE CIPHER)
    print('Decrypt')
    print('round[0].iinput', STATE0)
    print('round[0].ik_sch', roundkey[Nr])
    STATE1 = library.AddRoundKey(STATE0, roundkey[Nr])
    counter = 1
    print(f'round[{counter}].istart', STATE1)
    STATE2 = library.InvShiftRows(STATE1)
    print(f'round[{counter}].is_row', STATE2)
    STATE0 = library.InvSubBytes(STATE2)
    print(f'round[{counter}].is_box', STATE0)
    for i in range(Nr-1, 0, -1):
        counter += 1
        print(f'round[{counter}].ik_sch', roundkey[i])
        STATE1 = library.AddRoundKey(STATE0, roundkey[i])
        print(f'round[{counter}].istart', STATE1)
        STATE2 = library.InvMixColumns(STATE1)
        print(f'round[{counter}].im_col', STATE2)
        STATE3 = library.InvShiftRows(STATE2)
        print(f'round[{counter}].is_row', STATE3)
        STATE0 = library.InvSubBytes(STATE3)
        print(f'round[{counter}].is_box', STATE0)
    STATE0 = library.AddRoundKey(STATE0, roundkey[0])
    print(f'round[{counter}].message', STATE0)
