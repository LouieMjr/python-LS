# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

def determine_measurement_type():
    measurement_type = input('Do you want the area in Meters(m) or Square feet(sqft)? ')

    match measurement_type:
        case 'm'|'meters'|'Meters':
            measurement_type = 'Meters'
            area = area_of_room(measurement_type)
            print(f'The area of the room is {area[0]:,.2f} meters')

        case 'sqft'|'square feet'|'Square feet':
            measurement_type = 'Square feet'
            area = area_of_room(measurement_type)
            print(f'The area of the room is {area[1]:,.2f} square feet')

        case _:
            area = area_of_room(measurement_type)
            print(f'\nYou didnt specify correctly, so we gave you both:\nThe area of the room is {area[0]:,.2f} meters '
          f'and {area[1]:,.2f} square feet')

def area_of_room(measurement):
    try:
        width = float(input(f'\nEnter width of room in {measurement}: '))
        length = float(input(f'Enter length of room in {measurement}: '))
        one_square_meter = 10.7639

        area_in_meters = length * width
        area_in_squarefeet = area_in_meters * one_square_meter
        return (area_in_meters, area_in_squarefeet)
    except (UnboundLocalError, ValueError):
        print(UnboundLocalError, ValueError, TypeError)
        return area_of_room(measurement)

def display_area_of_room():
    determine_measurement_type()

display_area_of_room()