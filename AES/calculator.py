"""
    計算兩個16進位的數字，轉換成二進位之後相加，滿足GF(2)，最後在轉回16進位的數字。
    ex: 輸入數字: c9, 69
        11001001 + 01101001 = 10100000
        輸出結果: a0
"""
while True:
    print("輸入'exit'來退出計算機")
    hex1 = input("請輸入第一串16進位數字：")
    if hex1 == 'exit':
        break
    hex2 = input("請輸入第二串16進位數字：")
    if hex1 == 'exit':
        break

    # 檢查長度是否一致
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
        result_hex = hex(int(result_bin, 2))[2:].zfill((max_len + 3) // 4)

        print("輸出結果：", result_hex)
    else:
        print("長度不一致，請重新輸入")

