while True:
              num1 = input("Choose a number: ")
              num2 = input("Choose another number: ")
              print("Choose an option: ")
              opt = input(
                  "    Options are: +, -, * or /.\n    Wirte 'exit' to finish.\n"
              )
              if opt == "exit":
                            break
              elif opt == "+":
                            print("Result:", int(num1) + int(num2))
              elif opt == "-":
                            print("Result:", int(num1) - int(num2))
              elif opt == "*":
                            print("Result:", int(num1) * int(num2))
              elif opt == "/":
                            print("Result:", int(num1) / int(num2))
