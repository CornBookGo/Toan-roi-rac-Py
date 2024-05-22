import math

def modinv(a, m):
    # Sử dụng math.gcd để kiểm tra xem a và m có số nguyên tố cùng nhau hay không
    g = math.gcd(a, m)
    if g != 1:
        raise ValueError("Nghịch đảo mod không có")
    else:
        # Trả về giá trị modinv
        return pow(a, -1, m)

# Ví dụ: tính modinv của 80265707 modulo 724484437
result = modinv(13**10, 29)
print(result)
