def solution(phoneBook):
    answer = True
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            answer = False
            break

    return answer


