def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số từ người dùng
s1 = int(input("Nhập số nguyên thứ nhất: "))
s2 = int(input("Nhập số nguyên thứ hai: "))

# Gọi hàm để tính GCD và in kết quả
gcd = ucln(s1, s2)
print(f"Ước chung lớn nhất của {s1} và {s2} là {gcd}")
