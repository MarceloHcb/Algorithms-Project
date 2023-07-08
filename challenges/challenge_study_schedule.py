def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    students = 0
    for period in permanence_period:
        if not all(isinstance(p, int) for p in period):
            return None
        if period[0] <= target_time <= period[1]:
            students += 1
    return students
