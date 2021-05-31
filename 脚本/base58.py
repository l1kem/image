def b58encode(tmp:str) -> str:
	tmp = list(map(ord,tmp))
	temp = tmp[0]
	base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
	for i in range(len(tmp)-1):
		temp = temp * 256 + tmp[i+1]
	tmp = []
	while True:
		tmp.insert(0,temp % 58)
		temp = temp // 58
		if temp == 0:
			break
	temp = ""
	for i in tmp:
		temp += base58[i]
	return temp

def b58decode(tmp:str) -> str:
	import binascii
	base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
	temp = []
	for i in tmp:
		temp.append(base58.index(i))
	tmp = temp[0]
	for i in range(len(temp)-1):
		tmp = tmp * 58 + temp[i+1]
	return binascii.unhexlify(hex(tmp)[2:].encode("utf-8")).decode("UTF-8")

s = input("Please enter the ciphertext：")
print(b58decode(s))
