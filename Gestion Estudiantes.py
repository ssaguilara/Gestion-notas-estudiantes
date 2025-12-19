"""
Programa de gestion de notas de estudiantes. 
El programa debe permitir:
1.Registrar estudiantes (nombre, edad, notas, promedio, si aprueba)
2.Ver la información de los estudiantes
3.Calcular promedios
4.Salir del programa
"""

def menuOption():
    print("------------------------------")
    print("------------ Menu ------------")
    print("1. Register student")
    print("2. View student information")
    print("3. Calculate average grade")
    print("4. Exit")

# students = [{"id": 1, "nombre":"Sergio", "edad":32, "notas": 5 4 3, notaDefinitiva: 4, Aprueba}, ...]
students = []

def register():

    while True:
        nameInput = input("Enter name of student: ").strip().title() # Strip quito espacios extremos
        nameList = nameInput.split() # Split separo palabras en una lista
        # print(nameList)
        if not nameList: 
             print("Error: Name cannot be empty.")
             continue # Salta el resto del código dentro del bucle y regresa al principio del bucle, para la siguiente iteración, para volver a ingresar el nombre
        
        invalidName = False # Con esta variable definimos si continuamos en ciclando el while hasta que ingrese un nombre permitido
        for name in nameList:
            if not name.isalpha(): # valido cada palabra, si contiene solo letras devuelve un booleano True
                print(f"Error: '{name}'. Enter only letters.")
                invalidName = True
                break # salimos del for

        if not invalidName:  # si no se encontró ningún error
            fullName = " ".join(nameList)
            # print(f"Name entered: {fullName}")           
            break  # salimos del while         

    while True:
        ageInput = input("Enter age of student: ")
        try:
            age = int(ageInput)
            if age < 18 or age > 70:
                    print("Error: Age must be between 18 and 70")
                    continue
            # print(f"Age entered: {age}")
            break
        except ValueError:
            print(f"Error: '{ageInput}'. Enter only numbers")
    
    grades = []
    sumOfGrades = 0

    for i in range(3):
        while True:
            gradeInput = input(f"Enter grade #{i+1}: ")
            try:
                grade = float(gradeInput)

                if grade < 0 or grade > 5:
                    print("Error: Grade must be between 0 and 5.")
                    continue

                grades.append(grade)
                sumOfGrades += grade
                # print(f"Grade #{i+1} entered: {grade}")
                break

            except ValueError:
                print(f"Error: '{gradeInput}'. Enter only numbers.")

    averageGrades = round(sumOfGrades / len(grades),1)
    # averageGrades = round(sum(grades) / len(grades),1) # Otra opcion calcular promedios
    result = "Approves" if averageGrades >= 3 else "Disapproves"

    # print(grades)
    # print(len(grades))
    # print(averageGrades)

    student = {
        "id": len(students)+1,
        "name": fullName,
        "age": age,
        "grades": grades,
        "average": averageGrades,
        "result": result
    }

    students.append(student)
    # print(student)
    # print(students)

def view():

    if not students:
        print("There are not students registered")
    else:       
       for student in students:
            print("------------------------------")
            print(f"Id: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {' | '.join(str(g) for g in student['grades'])}") # Convertir cada valor de la lista en un string, para usar la funcion join e imprimir cada valor con su separador 
            print(f"Average: {student['average']}")
            print(f"Result: {student['result']}")

def calculate():

    # print(students)
    if not students:
        print("There are not students registered")
        return # aunque no devolvemos nada, terminamos la ejecucion de la funcion para evitar division por cero en el promedio

    average_grades = sum(student['average'] for student in students) / len(students)
    print(f"Average Grades Students: {average_grades:.1f}")
   
while True:
    menuOption()
    while True:
        print("------------------------------")
        optionInput = input("Enter option number: ")
        print("------------------------------")
        try:
            option = int(optionInput)
            break
        except:
            print(f"Error: '{optionInput}'. Enter only number option")

    if option == 1:
        register()
    elif option == 2:
        view()
    elif option == 3:
        calculate()
    elif option == 4:
        print("Exit")
        break
    else: 
        print("Error: Incorrect option selected")


    
