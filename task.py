import csv

def process_data(filename):
    red_count = 0
    yellow_count = 0
    green_count = 0
    red_time = 0
    yellow_time = 0
    green_time = 0
    green_active_times = []
    cycles = 0
    errors = 0

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            try:
                red, yellow, green, time_active, time = row
                red = int(red)
                yellow = int(yellow)
                green = int(green)
                time_active = int(time_active)
                time_parts = time.split(':')
                time_seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])

                if red + yellow + green != 1:
                    errors += 1
                else:
                    if red:
                        red_count += 1
                        red_time += time_active
                    elif yellow:
                        yellow_count += 1
                        yellow_time += time_active
                    elif green:
                        green_count += 1
                        green_time += time_active
                        green_active_times.append(time)

                    if red_count >= 1 and yellow_count >= 1 and green_count >= 1:
                        cycles += 1
                        red_count = yellow_count = green_count = 0

            except ValueError:
                errors += 1

    return red_count, yellow_count, green_count, red_time, yellow_time, green_time, green_active_times, cycles, errors

filename = r"C:\Users\Mantas-PC\Documents\pyTask\task\data.txt"


red_count, yellow_count, green_count, red_time, yellow_time, green_time, green_active_times, cycles, errors = process_data(filename)

print("Red =", red_count)
print("Yellow =", yellow_count)
print("Green =", green_count)
print("Red Time =", red_time, "seconds")
print("Yellow Time =", yellow_time, "seconds")
print("Green Time =", green_time, "seconds")
print("Times when Green was active:", green_active_times)
print("Number of complete cycles:", cycles)
print("Number of lines with mistakes:", errors)
