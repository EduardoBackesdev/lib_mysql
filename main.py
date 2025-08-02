from lib.libmain import libmain
def main():
    lib = libmain()
    lib.insert("users", ["name"], ["John Doe"])
    

if __name__ == "__main__":
    main()