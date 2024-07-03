def deleteLastChar(word: str) -> str:
    n="".join([word[i] for i in range(len(word)-1)])
    print(n)


deleteLastChar(input("Enter"))
