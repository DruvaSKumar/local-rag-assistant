from agents import route_query

if __name__ == "__main__":
    user_id = "user1"
    question = input("Ask something: ")
    print(route_query(user_id, question))