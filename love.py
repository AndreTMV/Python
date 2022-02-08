import time as t
TIEMPO: float = .5
CONTADOR_BESOS: int = 2
print("Te quiero besar una vez")
while True:
    print(f"Te quiero besar {CONTADOR_BESOS} veces")
    t.sleep(TIEMPO)
    if TIEMPO <= 0.01:
        TIEMPO = .01
    else:
        TIEMPO -= .01
    CONTADOR_BESOS += 1
