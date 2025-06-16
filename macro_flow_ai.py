from agents import macro_agent

if __name__ == "__main__":
    profile = "Male, 25 years old, 70kg"
    goal = "Gain muscle"
    result = macro_agent(profile, goal)
    print("Macro Plan:", result)