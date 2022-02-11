def solution(jobs):
    jobs.sort()
    job_time = []
    start_time = []
    answer = 0
    job_scheduler = []
    count = 0
    total_job_time = 0
    global_wait_time = 0
    
    for i in range(len(jobs)):
        job_time.append(jobs[i][1])
        start_time.append(jobs[i][0])
    
    while True:
        if len(start_time) == 1:
            job_scheduler.append(job_time[0])
            total_job_time = max(job_scheduler)
            print("계산식 : ", total_job_time, " - ", start_time[0], " + ", job_time[0])
            result_real = (total_job_time - abs(start_time[0])) + job_time[0] + global_wait_time
            print("중간 결과 : ", result_real)
            job_time.pop(0)
            start_time.pop(0)
            count += result_real
            break
        elif start_time[0] <= 0:
            print("Start_time 가장 낮은값 0 미만일때 들어옴")
            for i in range(len(job_time)):
                if  len(job_time) < 2:
                    break
                
                elif job_time[i] == min(job_time): # 최소값 찾기
                    print(job_time[i], min(job_time))
                    for j in range(len(job_scheduler)):
                        total_job_time = total_job_time + job_scheduler[j]
                    job_scheduler.append(job_time[i])
                    print("계산식 : ", total_job_time, " - ", start_time[i], " + ", job_time[i])
                    result_real = (total_job_time - abs(start_time[i])) + job_time[i] + global_wait_time
                    print("중간 결과 : ", result_real)
                    job_time.pop(i)
                    start_time.pop(i)
                    count += result_real
                    print(job_time[i], min(job_time))
                else:
                    break
        else:
            for i in range(len(job_time)):
                start_time[i] -= 1
                print("여기 어려워", start_time, job_time)
            global_wait_time += 1  
                     
    answer = count / len(job_scheduler)
    print("#######최종 결과 : ", answer, "\n", "job_scheduler : ", job_scheduler, "\n", "job_time : ", job_time, "\n", "start_time : ", start_time)
    return answer

solution([[0, 3], [2, 9], [1, 6]])

"""
  요청부터 종료까지
  대기1 자기6 = 7
  대기8(끝지점 - start_time) 자기9 = 17
  
 *** 실제작업 시작시간 (job_scheduler) - 시작시간 (start_time) + 진행시간 (job_timer)
  
  대기 구하는 방법
  
 
 11 / 
 """