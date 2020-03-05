current_time = int (input ("current_time"))
hours_to_wait = int (input ("time_to_wait_in_hours"))
total_time_of_a_day = int (24)
time_in_days = (hours_to_wait // total_time_of_a_day)
remaining_hours = (hours_to_wait % total_time_of_a_day)
final_time = (current_time + remaining_hours)

print(final_time)