import time

from PIL import Image
import numpy as np
import library


def input_img(image):
    """
        Convert image to matrix.
    :param image: img.jpg
    :return: matrix
    """

    # 打開圖片
    image = Image.open(image)

    # # 將圖片調整大小為8x8像素 (FOR CHECKING)
    # image = image.resize((8, 8))

    # 將圖片轉換為灰階模式
    gray_image = image.convert('L')

    # 將灰階圖像轉換為NumPy數組
    image_array = np.array(gray_image)

    # 將每個像素值轉換為16進位表示法
    hex_array = np.vectorize(lambda x: hex(x)[2:].zfill(2))(image_array)
    return hex_array


def AES_enc(image, key):
    # Only use keys with a length of 32
    Nr = 10

    roundkey = library.KeyExpansion(key, Nr)

    # START Encrypt
    STATE0 = library.XOR(image, roundkey[0])  # the STATE0 here is a string, need to change to List (TO BE A MATRIX)
    for i in range(1, Nr):
        STATE1 = library.SubBytes(STATE0)
        STATE2 = library.ShiftRows(STATE1)
        STATE3 = library.MixColumns(STATE2)
        STATE0 = library.AddRoundKey(STATE3, roundkey[i])
    STATE1 = library.SubBytes(STATE0)
    STATE2 = library.ShiftRows(STATE1)
    STATE0 = library.AddRoundKey(STATE2, roundkey[Nr])
    return STATE0


def AES_dec(image, key):
    # START Decrypt (EQUIVALENT INVERSE CIPHER)
    Nr = 10

    roundkey = library.KeyExpansion(key, Nr)

    STATE1 = library.AddRoundKey(image, roundkey[Nr])
    STATE2 = library.InvShiftRows(STATE1)
    STATE0 = library.InvSubBytes(STATE2)
    for i in range(Nr-1, 0, -1):
        STATE1 = library.AddRoundKey(STATE0, roundkey[i])
        STATE2 = library.InvMixColumns(STATE1)
        STATE3 = library.InvShiftRows(STATE2)
        STATE0 = library.InvSubBytes(STATE3)
    STATE0 = library.AddRoundKey(STATE0, roundkey[0])
    return STATE0


def Encrypt(img_matrix):
    # Generate a decimal matrix for overwrite
    decimal_array = np.vectorize(lambda x: int(x, 16))(img_matrix)

    # 正常來說這裏要先判斷image長度需不需要Padding
    for row in range(len(img_matrix)//4):
        for column in range(len(img_matrix[0])//4):
            # 提取最左上角的4x4方塊
            sub_matrix = img_matrix[4*row:4*row+4, 4*column:4*column+4]
            # 將方塊展平為一維數組
            flattened_array = sub_matrix.flatten(order='F')
            # 將數組中的元素連接為字符串
            sub_img_str = ''.join(str(x) for x in flattened_array)


            print("start encrypt submatrix[%d][%d]" % (row, column))
            # Encrypt
            enc_sub_img = AES_enc(sub_img_str, key)
            # Convert the encrypted result to decimal
            enc_sub_img_lst = [int(enc_sub_img[i:i + 2], 16) for i in range(0, len(enc_sub_img), 2)]
            # 將列表轉換為4x4矩陣
            submatrix = np.array(enc_sub_img_lst).reshape((4, 4))
            # 從列開始填充矩陣 (.T就是從列開始)
            decimal_array[4*row:4*row+4, 4*column:4*column+4] = submatrix.T

            # # Get the submatrix encrypted image
            # image = Image.fromarray(decimal_array)
            # image = image.convert("L")
            # # 保存圖片
            # image.save('image/encrypt_image_%d_%d.bmp' % (row, column))
    return decimal_array


def Decrypt(img_matrix):
    # Generate a decimal matrix for overwrite
    decimal_array = np.vectorize(lambda x: int(x, 16))(img_matrix)

    # 正常來說這裏要先判斷image長度需不需要Padding
    for row in range(len(img_matrix) // 4):
        for column in range(len(img_matrix[0]) // 4):
            # 提取最左上角的4x4方塊
            sub_matrix = img_matrix[4 * row:4 * row + 4, 4 * column:4 * column + 4]
            # 將方塊展平為一維數組
            flattened_array = sub_matrix.flatten(order='F')
            # 將數組中的元素連接為字符串
            sub_img_str = ''.join(str(x) for x in flattened_array)

            print("start decrypt submatrix[%d][%d]" % (row, column))
            # Encrypt
            dec_sub_img = AES_dec(sub_img_str, key)
            # Convert the encrypted result to decimal
            dec_sub_img_lst = [int(dec_sub_img[i:i + 2], 16) for i in range(0, len(dec_sub_img), 2)]
            # 將列表轉換為4x4矩陣
            submatrix = np.array(dec_sub_img_lst).reshape((4, 4))
            # 從列開始填充矩陣 (.T就是從列開始)
            decimal_array[4 * row:4 * row + 4, 4 * column:4 * column + 4] = submatrix.T

            # # Get the submatrix encrypted image
            # image = Image.fromarray(decimal_array)
            # image = image.convert("L")
            # # 保存圖片
            # image.save('image/decrypt_image_%d_%d.bmp' % (row, column))
    return decimal_array


if __name__ == '__main__':
    key = '000102030405060708090a0b0c0d0e0f'

    # 根據輸入值選擇不同的程式功能
    choice = input("Enter 'enc' for encryption or 'dec' for decryption: ")
    if choice == 'enc':
        img = 'Lena-image-with-a-256-256-size.bmp'
        img_matrix = input_img(img)

        start_time = time.time()
        # start encrypt
        enc_matrix = Encrypt(img_matrix)
        end_time = time.time()
        print("Total encrypt time:", end_time-start_time)

        # 將矩陣轉換為圖片
        image = Image.fromarray(enc_matrix)
        image = image.convert("L")
        # 保存圖片
        image.save('encrypt_image.bmp')

    elif choice == 'dec':
        img = 'encrypt_image.bmp'
        img_matrix = input_img(img)

        start_time = time.time()
        # start decrypt
        dec_matrix = Decrypt(img_matrix)
        end_time = time.time()
        print("Total decrypt time:", end_time-start_time)

        # 將矩陣轉換為圖片
        image = Image.fromarray(dec_matrix)
        image = image.convert("L")
        # 保存圖片
        image.save('decrypt_image.bmp')
    else:
        print("Invalid choice")


"""
    === time record ===
    Lena_512x512.bmp
    encrypt time: 89.68162441253662 (sec)
    decrypt time: 233.07298874855042 (sec)
    
    Lena_256x256.bmp
    encrypt time: 22.418922662734985 (sec)
    decrypt time: 58.81337785720825 (sec)
"""
