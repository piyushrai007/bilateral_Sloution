SELECT patients.patient_id, patients.patient_name
FROM patients
INNER JOIN medical_tests ON patients.patient_id = medical_tests.patient_id
WHERE medical_tests.test_name = 'MRI' AND medical_tests.test_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH);
