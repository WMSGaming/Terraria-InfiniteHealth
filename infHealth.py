import pymem.process

healthOffset = 0x1D3EE48C

pm = pymem.Pymem("Terraria.exe")


def main():
    while True:
        pm.write_int(healthOffset, 100)


main()
