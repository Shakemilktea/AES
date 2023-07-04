import numpy as np

# 16進位表示法的數組
hex_array = np.array([['01', '02', '0A'], ['0B', '1F', '10']])

# 將16進位表示法的數組還原為10進位的NumPy數組
decimal_array = np.vectorize(lambda x: int(x, 16))(hex_array)

# 打印還原後的NumPy數組
print(decimal_array)