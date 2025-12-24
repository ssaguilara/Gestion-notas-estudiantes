"""
Programa de gestion de notas de estudiantes. 
El programa debe permitir:
1.Registrar estudiantes (nombre, edad, notas, promedio, si aprueba)
2.Ver la información de los estudiantes
3.Calcular promedios
4.Salir del programa
"""

students = []
lastCurrentId = 0 

def menuOption():
    print("------------------------------")
    print("------------ Menu ------------")
    print("1. Register student")
    print("2. View student information")
    print("3. Calculate average grade")
    print("4. Delete Student")
    print("5. Exit")

def getValidName(): 
        while True:
            nameInput = input("Enter name of student: ").strip().title() # Strip quito espacios extremos
            nameList = nameInput.split() # Split separo palabras en una lista 
            # print(nameList)
            if not nameList: 
                print("Error: Name cannot be empty.")
                continue # Salta el resto del código dentro del bucle y regresa al principio del bucle, para la siguiente iteración, para volver a ingresar el nombre 
            if all(name.isalpha() for name in nameList): # isalpha(): valido cada nombre, si contiene solo letras devuelve un booleano True, si toda(all) la lista es true significa que el nombre completo esta bien
                return " ".join(nameList)   
                                      
            print(f"Error: '{nameInput}'. Enter only letters.")
                    
def getValidAge():
    while True:
        ageInput = input("Enter age of student: ")
        try:
            age = int(ageInput)
            if 18 <= age <= 70:
                return age         
            print("Error: Age must be between 18 and 70")
        except ValueError:
            print(f"Error: '{ageInput}'. Enter only numbers")

def getValidGrades():
    grades = []
    for i in range(3):
        while True:
            gradeInput = input(f"Enter grade #{i+1}: ")
            try:
                grade = float(gradeInput)
                if 0 <= grade <= 5:
                    grades.append(grade)
                    break              
                print("Error: Grade must be between 0 and 5.")
            except ValueError:
                print(f"Error: '{gradeInput}'. Enter only numbers.")
    return grades

def getAverageGrades(grades):
    return round(sum(grades) / len(grades),1)

def getResult(averageGrades):
    return "Approves" if averageGrades >= 3 else "Disapproves"

def registerStudent(students,lastCurrentId):
    idStudent = lastCurrentId
    name = getValidName() 
    age = getValidAge()
    grades = getValidGrades()
    averageGrades = getAverageGrades(grades) 
    result = getResult(averageGrades)   
    # print(name)
    # print(ages)
    # print(grades)
    # print(len(grades))
    # print(averageGrades)
    # print(result)

    student = {
        "id": idStudent,
        "name": name,
        "age": age,
        "grades": grades,
        "average": averageGrades,
        "result": result,
    }

    print(student)
    students.append(student) #no es necesario return devolveria solo una referencia
    print(students)
    print("Student added successfully")

        
def viewStudentList(students):
    if not students:
        print("There are not students registered")
    else:     
        for student in students:
            print("------------------------------")
            print(f"Id: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {' | '.join(str(g) for g in student['grades'])}") # Convertir cada valor del generador en un string, para usar la funcion join e imprimir cada valor con su separador 
            print(f"Average: {student['average']}")
            print(f"Result: {student['result']}")

def calculateGeneralAverage(students):
    # print(students)
    if not students:
        print("There are not students registered")
        return # aunque no devolvemos nada, terminamos la ejecucion de la funcion para evitar division por cero en el promedio

    averageGrades = sum(student['average'] for student in students) / len(students)
    print(f"Average Grades Students: {averageGrades:.1f}")

def getValidId():
    while True:
        idStudentInput = (input("Enter number ID for delete student: "))
        try:
            idStudentDelete= int(idStudentInput)
            if idStudentDelete > 0:
                return idStudentDelete  
            
            print("Error: The ID must be a positive number")         
        except ValueError:
            print(f"Error: '{idStudentInput}'. Enter only numbers.")

def deleteStudent(students):
    if not students:
        print("There are not students registered")
    else:
        idStudentDelete= getValidId()
        newStudents = [student for student in students if student["id"] != idStudentDelete] #Crear una nueva lista con todos los estudiantes excepto el que tiene el id que quiero borrar

        print("Student not found") if len(newStudents) == len(students) else print("Student deleted successfully")
        # Validar si el id ingresado si exite 

        return newStudents


def getValidOption():
        while True:
            print("------------------------------")
            optionInput = input("Enter option number: ")
            print("------------------------------")
            try:
                return int(optionInput)               
            except ValueError:
                print(f"Error: '{optionInput}'. Enter only number option")

while True:
    menuOption()
    option = getValidOption()
    if option == 1:
        lastCurrentId= lastCurrentId + 1
        registerStudent(students,lastCurrentId)    
    elif option == 2:
        viewStudentList(students)
    elif option == 3:
        calculateGeneralAverage(students)
    elif option == 4:
        students = deleteStudent(students)
    elif option == 5:
        print("Exit")
        break
    else: 
        print("Error: Incorrect option selected")


    
