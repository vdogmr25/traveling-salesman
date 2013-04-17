def main():
    listA = ["one","two","three","four", "five"]
    i = 1
    j = 4
    listB = listA[:i]
    listB.extend(reversed(listA[i:j]))
    listB.extend(listA[j:])

    print listB

main()
