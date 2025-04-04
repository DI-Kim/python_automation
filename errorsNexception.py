# errors and exceptions
def div21by(divisor):
    try:
        return 21 / divisor
    except:
        print("Error: Division by zero is not allowed")
        return None


def div42by(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    finally:
        print("Execution completed")


div42by(0)
