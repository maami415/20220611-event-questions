for num in range(1, 101):
    string = ''

    # ここから記述
    # numが15で割り切れるなら
    if num % 15 == 0:
        # stringに'FizzBuzz'を代入
        string = 'FizzBuzz'
    # numが3で割り切れて5で割り切れないなら
    elif num % 3 == 0:
        # stringに'Fizz'を代入
        string = 'Fizz'
    # numが5で割り切れて3で割り切れないなら
    elif num % 5 == 0:
        # # stringに'Buzz'を代入
        string = 'Buzz'
    # numが3でも5でも割り切れないなら
    else:
        # stringにnumの数値を代入
        string = num
    # ここまで記述

    print(string)