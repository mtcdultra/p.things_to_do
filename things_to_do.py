def to_do_generator():

    project_name = input("Project name: ").replace(" ","_")
    to_do_name = input("To-Do name: ").replace(" ","_")
    initial_number = int(input("First number: "))
    final_number = int(input("Final number: "))

    project_default = "things:///add-project?title="
    to_do_default = "to-dos="
    to_dos = ""

    result = project_default + project_name + "&" + to_do_default

    for number in range(initial_number,final_number+1):
        to_dos = to_dos + to_do_name + str(number) + "%0A"
        
    return result + to_dos


print(to_do_generator())