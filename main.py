from lib.libmain import libmain
def main():
    lib = libmain()
    lib.update("users", ["users"], ["Eduardo"])
    

if __name__ == "__main__":
    main()