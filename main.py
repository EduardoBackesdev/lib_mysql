from lib.libmain import libmain
def main():
    lib = libmain()
    lib.update("users", ["nome", "email"], ["Eduardo", "eduardo@hotmail.com"])
    

if __name__ == "__main__":
    main()