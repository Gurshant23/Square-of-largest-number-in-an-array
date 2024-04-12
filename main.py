def square_of_largest(arr):
    if not arr:
        return None  # Return None if the array is empty

    max_element = max(arr)
    return max_element ** 2


def main():
    try:
        total_elements = int(input("Enter the total number of elements: "))
        if total_elements <= 0:
            print("Total number of elements should be a positive integer.")
            return

        array = []
        for i in range(total_elements):
            element = int(input(f"Enter element {i+1}: "))
            array.append(element)

        result = square_of_largest(array)
        if result is not None:
            print(f"The square of the largest element is: {result}")
        else:
            print("The array is empty.")

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()