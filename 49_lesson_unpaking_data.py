from struct import *


# Data package
packed_data = pack('iii', 30,23,13)


#Unpacked data
udta = unpack("iii", packed_data)
print(udta)
