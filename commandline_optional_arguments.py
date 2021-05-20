#These are optional arguments and optional argumentsare can be skipped
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--operation",help="operation",choices=["add","subtract","multiply"])
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
    result = None
    
    if args.operation=="add":
        result = int(args.number1)+int(args.number2)
    elif args.operation=="subtract":
        result = int(args.number1)-int(args.number2)
    elif args.operation=="multiply":
        result = int(args.number1)*int(args.number2)
    else:
        print("unsupported operation")
    
    print("result : ",result)
    
    
'''
python commandline_optional_arguments.py --number1 5 --number2 4 --operation add   # positions of arguments are not fixed and argumnets are also optional 

python commandline_optional_arguments.py --number1 5 --number2 4 # also works
'''    