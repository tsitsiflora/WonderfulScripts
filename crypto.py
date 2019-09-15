# Run this code and use the output to proceed to the next stage

from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

message = b'gAAAAABdVCJP0miXpf8nAA0u3l3RfirB0Hy9pJflqIKiRNB_Lv0UncaVLBvz11x6pck2lPsRy7TYvX7Gxyx4NKgJLHoeeKXS4u133aMCz0-gN7n60G5aOSo='


def main():
   f = Fernet(key)
   print(f.decrypt(message))


if __name__ == "__main__":
   main()
