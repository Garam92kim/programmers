def solution(jobs):
    jobs.sort()
    job_time = []
    start_time = []
    answer = 0
    job_scheduler = []
    count = 0
    
    for i in range(len(jobs)):
        job_time.append(jobs[i][1])
        start_time.append(jobs[i][0])
        
    while True:
        if len(start_time) == 1:
            print("연산 전 !!!!!!!!!!!!!! \n", "job_scheduler : ", job_scheduler, "\n", "job_time : ", job_time, "\n", "start_time : ", start_time)
            job_scheduler.append(start_time[0])
            count += job_time[0]
            job_time.pop(0)
            start_time.pop(0)
            print("연산 후 @@@@@@@@@@@@ \n", "job_scheduler : ", job_scheduler, "\n", "job_time : ", job_time, "\n", "start_time : ", start_time)
            break
        elif start_time[0] <= 0:
            for i in range(len(job_time)):
                if job_time[i] < 
            
            print("연산 전 !!!!!!!!!!!!!! \n", "job_scheduler : ", job_scheduler, "\n", "job_time : ", job_time, "\n", "start_time : ", start_time)
            job_scheduler.append(start_time[0])
            count += job_time[0]
            start_time[1] -= job_time[0] #
            job_time.pop(0)
            start_time.pop(0)
            print("연산 후 @@@@@@@@@@@@@ \n", "job_scheduler : ", job_scheduler, "\n", "job_time : ", job_time, "\n", "start_time : ", start_time)
        
        #1ms (진입시간) 부터 대기하다 3ms(0번이 끝나는 시점)에서 시작 대기시간 2ms, 진행시간9ms = 11ms
        #2ms (진입시간) 부터 대기하다 14ms(1번이 끝나는 시점)에서 시작 대기시간12ms, 진행시간6ms = 18ms
        
        
    for i in range(len(job_scheduler)):
        count += abs(job_scheduler[i])
    answer = count / len(job_scheduler)
    print("#######최종 결과 : ", answer, "\n", "job_scheduler : ", job_scheduler, "\n", "job_time : ", job_time, "\n", "start_time : ", start_time)
    return answer

solution([[0, 3], [1, 9], [2, 6]])