DELIMETER = ","

def collectWords():
    CWords = []
    while True:
        CWord = input("Insert word(empty stops): ")
        if CWord == "":
            break
        CWords.append(CWord)
    return DELIMETER.join(CWords)

def analyseWords(PWords):
    AWords = PWords.split(DELIMETER)
    Words = len(AWords)
    Characters = sum(len(Word) for Word in AWords)
    Avg = Characters / Words
    if Characters == 0:
        print("- 0 Words")
    else:
        print(f"- {Words} Words")
    print(f"- {Characters} Characters")
    print("- {:.2f} Average word length".format[Avg])

def main():
    print("Program starting.")
    Words = collectWords()
    analyseWords(Words)
    print("Program ending.")

main()