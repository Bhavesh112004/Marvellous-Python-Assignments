import MarvellousNum as mp


def main():

    print("Enter the count of elements in list : ")
    Size = int(input())

    data = list()

    for i in range(Size):
      print("Enter the element : ")
      ele = int(input())
      data.append(ele)
  

    SumPrint = mp.sum_primes_in_list(data)
    print("The sum of primes is : ",SumPrint)


if __name__ == "__main__":
    main()