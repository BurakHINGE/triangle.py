while True:
    def triangle():

        size = int(input("Enter the size of the triangle (minimum 2): "))

        if size < 2:
            print("Please enter a number 2 or greater.")

        else:
            for i in range(1, size + 1):
                for k in range(i):
                    print("*", end=" ")
                print()
                
    triangle()
