def get_hello_world() -> str:
    return "Hello World!"


# This construct runs the code as script but not when it is imported
if __name__ == "__main__":
    print(get_hello_world)
