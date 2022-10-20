def main():
    print("Введите требуемое число фибаначи")
    Nfib = int(input())
    print(Fibanachi(Nfib))

def Fibanachi(value):
    i=0
    Ni=0
    Ni_1 =1
    while i<value:
        Nvr = Ni
        Ni +=Ni_1
        Ni_1=Nvr
        i+=1
    return Ni

if __name__ == '__main__':
    main()
