import pprint
known1 = dict()
known2 = dict()


# using nested dictionary
def ack1(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 0:
        print("m and n should be non-negative integers")
        return None
    elif m == 0:
        return known1.setdefault(m, {}).setdefault(n, n+1)
    elif m > 0 and n == 0:
        return known1.setdefault(m, {}).setdefault(n, ack1(m-1, 1))
    else:
        return known1.setdefault(m, {}).setdefault(n, ack1(m-1, ack1(m, n-1)))


# using dual key
def ack2(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 0:
        print("m and n should be non-negative integers")
        return None
    elif m == 0:
        return known2.setdefault((m, n), n+1)
    elif m > 0 and n == 0:
        return known2.setdefault((m, n), ack2(m-1, 1))
    else:
        return known2.setdefault((m, n), ack2(m-1, ack2(m, n-1)))


# 3,4 = 125; 3,6 = 509
m = 3; n = 6
print("W/ Nested Dict:", ack1(m, n))
print("W/ dual key Dict:", ack2(m, n))
pprint.pprint(known2)
