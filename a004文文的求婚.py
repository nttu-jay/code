while True:
    try:
        year = int(input())
        if(year % 4 == 0):
            if(year % 100 == 0):
                if(year % 400 == 0):
                    print("閏年")
                else:
                    print("平年")
            else:
                print("閏年")
        else:
            print("平年")
    except EOFError:
        break