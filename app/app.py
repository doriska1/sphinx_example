#from app import ExampleModel
from model.model import ExampleModel

def main():
    """
    Main method
    """
    ExampleModel(2).first_method(1)
    print("ok")
    return None


if __name__ == "__main__":
    main()