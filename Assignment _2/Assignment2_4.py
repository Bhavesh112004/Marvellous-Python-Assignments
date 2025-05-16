def FactorsSum(No):
    cnt = 1
    factorsum = 0
    while (cnt <= No/2):
        if (No % cnt == 0):
            factorsum = factorsum + cnt
        cnt = cnt + 1
    return factorsum

def main():
    result = FactorsSum(12)
    print(result)
if __name__ == "__main__":
    main()