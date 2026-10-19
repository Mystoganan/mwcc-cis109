import argparse
import sys

def get_word_count(data):
    toks = data.split()
    return len(toks)

def transform_upper(data):
    uppercase_text = data.upper()
    return uppercase_text

def transform_lower(data):
    lowercase_text = data.lower()
    return lowercase_text

def filtered_data(data):
    if (len(data.split()))>= 3:
        filtered_text = data
        return filtered_text
    elif():
        filtered_text = ""
        return filtered_text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", help="Transformer action [count | lower | upper]")
    parser.add_argument("-d", "--data", help="data to tranfer")
    args = parser.parse_args()

    if args.action:
        print(f"Action:{args.action}")

    if args.data:
        print(f"Data:{args.data}")
        
    match args.action:
        case "count":
            print(f"Word Count:{get_word_count(args.data)}")
        case "upper":
            print(f"Uppercase:{transform_upper(args.data)}")
        case "lower":
            print(f"Lowercase:{lowercase_text(args.data)}")
        case "filter":
            print(f"Filtered: {filtered_data(args.data)}")


main()