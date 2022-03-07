def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        array_slice = array[commands[i][0]-1:commands[i][1]]
        sorted_list = sorted(array_slice) # sort 안되는 이유 ? -> 이미 정렬된 list는 다시 sort 할수 없음(?) PYTHON 특징인듯
        answer.append(sorted_list[commands[i][2]-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])