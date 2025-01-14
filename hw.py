import math

def trigonometric_values():
    print("Welcome to the Trigonometric Value Finder!")
    print("Choose the input type:")
    print("1. Degrees")
    print("2. Radians")
    
    choice = input("Enter your choice (1 or 2): ")
    if choice not in ('1', '2'):
        print("Invalid choice. Please select 1 or 2.")
        return
    
    angle = float(input("Enter the angle: "))
    
    if choice == '1':
        angle_in_radians = math.radians(angle)
    else:
        angle_in_radians = angle

    sin_value = math.sin(angle_in_radians)
    cos_value = math.cos(angle_in_radians)
    tan_value = math.tan(angle_in_radians)

    print("\nTrigonometric Values:")
    print(f"Sin: {sin_value}")
    print(f"Cos: {cos_value}")
    
    if cos_value != 0:
        print(f"Tan: {tan_value}")
    else:
        print("Tan: Undefined (division by zero)")

if __name__ == "__main__":
    trigonometric_values()
