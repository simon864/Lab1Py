def to_number(string: str) -> int:
    try:
        number = int(string)
    except ValueError:
        print("Содержание строки – не число!")
        return to_number(input())
    
    return number