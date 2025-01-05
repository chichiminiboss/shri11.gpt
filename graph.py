import matplotlib.pyplot as plt

# Function to handle input with validation
def get_input(prompt, cast_func=str, validation=None):
    while True:
        try:
            value = cast_func(input(prompt))
            if validation and not validation(value):
                raise ValueError("Validation failed.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

# Function to create a graphv
def create_graph(graph_type="Line Graph"):
    print(f"\n--- Creating a {graph_type} ---")
    title_label = input("Enter the title of the graph: ")
    x_label = input("Enter the label for the x-axis: ")
    y_label = input("Enter the label for the y-axis: ")

    num_points = get_input("How many data points do you want to enter? ", int, lambda x: x > 0)

    x_values, y_values = [], []
    for i in range(num_points):
        x = get_input(f"Enter the x value for data point {i + 1}: ", float)
        y = get_input(f"Enter the y value for data point {i + 1}: ", float)
        x_values.append(x)
        y_values.append(y)

    plot_graph(x_values, y_values, title_label, x_label, y_label, graph_type)
    return x_values, y_values, title_label, x_label, y_label, graph_type

# Function to plot and save the graph
def plot_graph(x_values, y_values, title_label, x_label, y_label, graph_type):
    plt.figure(figsize=(8, 6))
    if graph_type == "Line Graph":
        plt.plot(x_values, y_values, label=title_label, marker='o')
    elif graph_type == "Bar Graph":
        plt.bar(x_values, y_values, label=title_label)
    elif graph_type == "Pie Chart":
        plt.pie(y_values, labels=x_values, autopct='%1.1f%%')
    elif graph_type == "Histogram":
        plt.hist(y_values, bins=len(x_values), label=title_label)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title_label)
    if graph_type != "Pie Chart":
        plt.legend()
    plt.savefig(f"{title_label}.png")
    plt.show()
    print(f"Graph saved as '{title_label}.png'\n")

# Function to modify a graph
def modify_graph(x_values, y_values, title_label, x_label, y_label, graph_type):
    print("\n--- Modify Graph ---")
    if get_input("Do you want to modify the title? (yes/no): ", str).lower() == "yes":
        title_label = input("Enter the new title: ")

    if get_input("Do you want to modify the x-axis label? (yes/no): ", str).lower() == "yes":
        x_label = input("Enter the new x-axis label: ")

    if get_input("Do you want to modify the y-axis label? (yes/no): ", str).lower() == "yes":
        y_label = input("Enter the new y-axis label: ")

    if get_input("Do you want to modify data points? (yes/no): ", str).lower() == "yes":
        x_values.clear()
        y_values.clear()
        num_points = get_input("How many data points do you want to enter? ", int, lambda x: x > 0)
        for i in range(num_points):
            x = get_input(f"Enter the x value for data point {i + 1}: ", float)
            y = get_input(f"Enter the y value for data point {i + 1}: ", float)
            x_values.append(x)
            y_values.append(y)

    plot_graph(x_values, y_values, title_label, x_label, y_label, graph_type)

# Function to choose the graph type
def get_graph_choice():
    print("\n--- Choose the type of graph ---")
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Pie Chart")
    print("4. Histogram")
    choice = get_input("Enter your choice (1-4): ", int, lambda x: 1 <= x <= 4)
    return ["Line Graph", "Bar Graph", "Pie Chart", "Histogram"][choice - 1]

# Main menu function
def main_menu():
    print("\n-- Let's Make a Graph --")
    print("------------------------------------------------------")
    x_values, y_values, title_label, x_label, y_label, graph_type = [], [], None, None, None, None

    while True:
        print("\n1. Create a new graph")
        print("2. Modify the existing graph")
        print("3. Exit")
        choice = get_input("Enter your choice (1-3): ", int, lambda x: 1 <= x <= 3)

        if choice == 1:
            graph_type = get_graph_choice()
            x_values, y_values, title_label, x_label, y_label, graph_type = create_graph(graph_type)

        elif choice == 2:
            if not x_values:
                print("No graph exists to modify. Please create one first.")
            else:
                modify_graph(x_values, y_values, title_label, x_label, y_label, graph_type)

        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main_menu()
