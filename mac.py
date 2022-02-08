import random
for number in range(20):
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    print(':'.join(map(lambda x: "%02x" % x, mac)))
