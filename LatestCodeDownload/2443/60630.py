print(''.join([q[len(q) >> 1 : ] for q in sorted([p * 2 for p in input("")[1 : -1].split(',')], reverse = True)]))