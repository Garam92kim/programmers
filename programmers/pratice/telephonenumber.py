def solution(phone_book):
    phone_book.sort(key=len)
    prefix_contains = set()
    for phone_number in phone_book:
        print ("1", phone_number)
        for i in range(1, len(phone_number)+1):
            prefix = phone_number[:i]
            print ("2", prefix)
            if prefix_contains.__contains__(prefix):
                print("FALSE")
                return False
        prefix_contains.add(phone_number)
        print(prefix_contains)
    return True

solution(["112", "342", "23215", "74", "112345"])