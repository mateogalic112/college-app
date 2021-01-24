# Function for checking if adding subject is valid based on ects for current semester
def can_add_subject_ects(student, subject, selected_semester):

    enrolls = student.enroll_set.all()
    ects_in_semestar = subject.bodovi
    for row in enrolls:
        if student.status == 'REDOVNI' and row.predmet.sem_redovni == selected_semester:
            ects_in_semestar += row.predmet.bodovi
        elif student.status == 'IZVANREDNI' and row.predmet.sem_izvanredni == selected_semester:
            ects_in_semestar += row.predmet.bodovi
    
    if ects_in_semestar > 30:
        return False
    return True

# Function for checking if adding subject is valid based on previous ects points
def can_add_subject_prev_ects(student, subject, selected_semester):
    enrolls = student.enroll_set.all()
    if selected_semester > 2:
        bound = selected_semester % 2 == 1 and selected_semester or selected_semester - 1
        for i in range(1, bound):
            target = student.status == 'REDOVNI' and 15 or 6
            current_ects = 0
            for row in enrolls:
                if student.status == 'REDOVNI':
                    if row.predmet.sem_redovni == i and row.status == 'passed':
                        current_ects += row.predmet.bodovi
                elif student.status == 'IZVANREDNI':
                    if row.predmet.sem_izvanredni == i and row.status == 'passed':
                        current_ects += row.predmet.bodovi
            if current_ects < target:
                return False
        return True