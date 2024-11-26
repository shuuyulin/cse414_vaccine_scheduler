

select_Cusername_details = "SELECT * FROM Caregivers WHERE Username = %s"

select_Pusername_details = "SELECT * FROM Patients WHERE Username = %s"

get_caregiver_details = "SELECT Salt, Hash FROM Caregivers WHERE Username = %s"

get_patient_details = "SELECT Salt, Hash FROM Patients WHERE Username = %s"

search_caregiver_details = \
"\
    SELECT\
        C.Username\
    FROM\
        Caregivers AS C,\
        Availabilities AS A\
    WHERE\
        C.Username = A.Username AND\
        A.Time = %s\
    ORDER BY\
        C.Username\
"

search_doses_details = "SELECT * FROM Vaccines"

show_appointment_caregiver_details = \
"\
    SELECT\
        R.Id,\
        R.Vname,\
        R.Time,\
        R.Pusername\
    FROM\
        Reservations AS R\
    WHERE\
        R.Cusername = %s\
"

show_appointment_patient_details = \
"\
    SELECT\
        R.Id,\
        R.Vname,\
        R.Time,\
        R.Cusername\
    FROM\
        Reservations AS R\
    WHERE\
        R.Pusername = %s\
"