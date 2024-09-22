sage: for i in range(1000000):
        x = leak + 2 * n + i * n
        u = (1 + sqrt(1 + 4 * x)) / 2
        u = int(u)
        phi = n - u + 1
        d = pow(int(e) , -1 , int(phi))
        m = pow(int(ciph) , int(d) , int(n))
        try:
            m = bytes.fromhex(hex(m)[2:])
        except: ValueError
        else:
            if plain in m:
                print(m)
                break
