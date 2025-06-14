# MyFeature.py
# A basic Python feature demonstrating a simple functionality

def greet_user(name):
    """
    Function to greet the user with their name.
    :param name: str - Name of the user
    :return: str - Greeting message
    """
    return f"Hello, {name}! Welcome to MyFeature."

if __name__ == "__main__":
    # Example usage
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
    print("Welcome to MyFeature!")