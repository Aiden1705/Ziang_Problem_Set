def temp_tester(temp:float):
    def creature(temp2:float):
        if temp2 > temp+1:
            return False
        elif temp2 < temp-1:
            return False
        else:
            return True
    return creature

human_tester = temp_tester(37)
chicken_tester = temp_tester(41.1)
print(chicken_tester(42))
print(human_tester(42))
print(chicken_tester(43))
print(human_tester(35))
print(human_tester(98.6))