
from agents.supervisor import route_query

def main():
    print("AI Career Assistant – Multi-Agent System")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask something: ")
        if query.lower() == "exit":
            break

        response = route_query(query)
        print("\nResponse:")
        print(response)
        print("-" * 40)

if __name__ == "__main__":
    main()
