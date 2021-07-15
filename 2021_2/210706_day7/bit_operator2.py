# 테트리스 벽돌을 출력해보자
brick = (0x0660, 0x0F00, 0x2222, 0x6220, 0x4460, 0x4640, 0x7200, 0x6300,0x4620)
for i in brick:
    mask = 0b1000000000000000
    for j in range(0,16):
        print('■' if (mask & i) == mask else '□', end='')
        if (j+1)%4==0:
            print()
        mask >>= 1
    print()