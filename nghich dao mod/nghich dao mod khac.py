def tim_kq(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

so = 80265707
mod = 724484437

kq = tim_kq(so, mod)

if kq is not None:
    print("Nghịch đảo của", so, "theo modulo", mod, "là:", kq)
else:
    print("Không tồn tại nghịch đảo của", so, "theo modulo", mod)
