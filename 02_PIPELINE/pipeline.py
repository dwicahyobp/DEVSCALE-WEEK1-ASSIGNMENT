from function import generate_raw_response, summarize, generate_structured_response
from models import Recipee

if __name__ == "__main__":
    user_message = input("Enter your recipe request: ")
    
    print("Raw Response:")
    raw = generate_raw_response(user_message)
    print(raw)

    print("\nSummarized Response:")
    summarized = summarize(raw)
    print(summarized)

    print("\nStructured Response:")
    structured_response = generate_structured_response(summarized, structured_response=Recipee)
    print(structured_response)