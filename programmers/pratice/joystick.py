def solution(name):
    answer = 0
    ascii_name = []
    cnt_hap = 0
    
    for character in name:
        ascii_name.append(ord(character))
    print(ascii_name)
    
    # 26개의 알파뱃
    # n 이면 앞으로 13번 or 뒤로 13번
        
    for i in range (len(ascii_name)):
        n_min = 65
        n_max = 91
        cnt = 0
        while True:
            if ascii_name[i] == 65 or ascii_name[i] == 90:
                print("A나 Z일때", ascii_name[i])
                break
            if ascii_name[i] > 78:
                n_max -= 1
                cnt += 1
                if n_max == ascii_name[i]:
                    print("here", cnt)
                    cnt_hap += cnt
                    break
            elif ascii_name[i] <= 78:
                n_min += 1
                cnt += 1
                if n_min == ascii_name[i]:
                    print("here", cnt)
                    cnt_hap += cnt
                    break
    if len(ascii_name) == 3:
        if ascii_name[1] == 65 or ascii_name[1] == 90:
            cnt_hap -= 1
    if ascii_name[0] == 65 or ascii_name[0] == 90:
        print('여기')
        cnt_hap -= 1
    if ascii_name[len(ascii_name)-1] == 65 or ascii_name[len(ascii_name)-1] == 90:
        cnt_hap -= 1

    print(cnt_hap + i)
    return cnt_hap + i

solution("JAN")