def study_schedule(permanence_period, target_time):
    if not len(permanence_period) or not target_time:
        return None
    count = 0

    for time in permanence_period:
        if type(time[0]) != int or type(time[1]) != int:
            return None
        if time[0] <= target_time <= time[1]:
            count += 1

    return count
