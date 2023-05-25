#include <iostream>
#include <string>
#include "person.h"
#include "university.h"
#include "student.h"
#include "teacher.h"
#include "teachingAssintant.h"


// Adicionar os .h dps

using namespace std;


int main(){
    
    cout<< "---------Pessoa-------" << endl;
    Person pessoa("Marco Reus", "31/05/1989", "Dortmunt <3");
    cout << pessoa.getName() << endl;
    cout << pessoa.getBirthDate() << endl;
    cout << pessoa.getSex() << endl;  
    
    cout<< "---Student---" << endl;
    Student aluno("Paulo", "17/09/1990", "Male", "UFSC", "EMB");
    cout << aluno.getName() << endl;
    cout << aluno.getBirthDate() << endl;
    cout << aluno.getSex() << endl;
    cout << aluno.getUname() << endl;
    cout << aluno.getDepartment() << endl;
    
    cout<< "---Teacher---" << endl;
    Teacher professor("Rafael", "09/12/1970", "Male", "UFSC", "EMB", "Prog III");
    cout << professor.getName() << endl;
    cout << professor.getBirthDate() << endl;
    cout << professor.getSex() << endl;
    cout << professor.getUname() << endl;
    cout << professor.getDepartment() << endl;
    cout << professor.getCourse() << endl;
    
    cout<< "---Teacher Assistant ---" << endl;
    TeachingAssistant assistente("Samira", "18/05/1990", "Female", "UFSC", "EMB","EE", "Prog III");
    cout << assistente.Student::getName() << endl;
    cout << assistente.Student::getBirthDate() << endl;
    cout << assistente.Student::getSex() << endl;
    cout << assistente.Student::getUname() << endl;
    cout << "Student's Departament" << endl;
    cout << assistente.Student::getDepartment() << endl;
    cout << "Teaching Departament" << endl;
    cout << assistente.Teacher::getDepartment() << endl;
    cout << assistente.getCourse() << endl;
    
    return 0;
    
    
}