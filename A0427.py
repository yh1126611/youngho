minutes = input(); minutes = int(minutes)
seconds = input(); seconds = int(seconds)
cuts = input(); cuts = int(cuts)
total_time = (minutes * 60) + seconds
cut_time = total_time / cuts
change_time = []

# Check
print("This is the total minutes: %d min." % minutes)
print("This is the total seconds: %d sec." % seconds)
print("This is the number of cuts: %d" % cuts)
print("This is the total time: %d sec." % total_time)
print("This is the time that will be alotted to each cut: %.2f sec." % cut_time)

cut_time_minute = 0
# Main calc'n.
for i in range(cuts):
    change_time.append(i * cut_time)
    if i * cut_time < 60:
        print ("Cut no. %d will begin at %.2f sec." % (i + 1, i * cut_time))
    else:
        for j in range(minutes):
            if (j + 1) * 60 <= i * cut_time :
                cut_time_minute = cut_time_minute + 1
            else:
                break
        print("Cut no. %d will begin at %d min. %.2f sec." % (i + 1, cut_time_minute, ((i * cut_time) - (cut_time_minute * 60))))
    cut_time_minute = 0