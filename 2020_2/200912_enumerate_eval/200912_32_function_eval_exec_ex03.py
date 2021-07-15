if 1:
    import pprint
    # 코드를 작성하세요




    # 하단의 코드는 global namespace에 이름이 등록되었는지 
    # 확인하는 코드입니다.
    for x in globals().items():
        if x[0][:len(name)] == name : print(*x)

