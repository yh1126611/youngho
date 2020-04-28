minutes = input("분"); minutes = int(minutes)
seconds = input("초"); seconds = int(seconds)
cuts = input("컷 수"); cuts = int(cuts)
total_time = (minutes * 60) + seconds
cut_time = total_time / cuts
change_time = []

# Check
print("이 영상은 총 %d분 %d초입니다." % (minutes, seconds))
print("초 단위로 환산하면 총 %d초입니다." % total_time)
print("이 영상에는 총 %d개의 컷이 들어갑니다." % cuts)
print("한 컷당 %.2f초의 시간이 배당됩니다." % cut_time)

cut_time_minute = 0
# Main calc'n.
for i in range(cuts):
    change_time.append(i * cut_time)
    if i * cut_time < 60:
        print ("%d번째 컷은 %.2f초에 시작합니다." % (i + 1, i * cut_time))
    else:
        for j in range(minutes):
            if (j + 1) * 60 <= i * cut_time :
                cut_time_minute = cut_time_minute + 1
            else:
                break
        print("%d번째 컷은 %d분 %.2f초에 시작합니다." % (i + 1, cut_time_minute, ((i * cut_time) - (cut_time_minute * 60))))
    cut_time_minute = 0