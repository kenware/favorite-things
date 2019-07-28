from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdMZGTEqSSjFg4T1E1LFJQZjGiGIJR3YuWH23JC7JSl9CmupAHlVD28ZuB8Z_hQPmJtXBubEPbjgvovuvr4Mnvkpacn-TqziG7aaQPtVpybWXJD1DKMcpXwylvkgjGhbQukDFXlCk4hJToEuLZ-w-OLZJ4rdwVPI8TTSTn4Us9QOFplK8='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
