p = next_prime(412341)
ec = EllipticCurve(GF(p) , [34123410 , 1])
p = ec.point((0, 1))
G = p * 3413431
k = next_prime(342083490)
PK = G * k
ec.cardinality()
d = inverse_mod(k , ec.cardinality()) # K * ? == cardinality() + 1
# d * PK == G => d * G*k == G => (k*d) * G % cardinality() == G
# k * d == Q * cardinality() + 1

應用
m * PK => other
other => (m * PK) * k == G * m


d == 私鑰
PK = G * K == 公鑰
