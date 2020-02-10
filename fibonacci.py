def main():
    a,b = 1,1
    num=eval(input("Please input a value for n: "))
    num_int=int(num-2)
    for i in range (num_int):
        a,b=b,a+b
    print(b)

main()
