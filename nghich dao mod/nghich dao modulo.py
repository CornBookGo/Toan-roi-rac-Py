def mod_inverse(a, m):
    """
    Tìm nghịch đảo modulo của số nguyên a theo modulo m
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1 # không tìm thấy nghịch đảo

# ví dụ:
a = 80265707
m = 724484437

print("Nghịch đảo modulo của", a, "theo modulo", m, "là", mod_inverse(a, m))
