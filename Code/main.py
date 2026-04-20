from graph.workflow import graph

user_input = input("Enter your travel request: ")

result = graph.invoke({
    "input": user_input
})

print("\n=== FINAL RESULT ===")
print(result.get("final"))