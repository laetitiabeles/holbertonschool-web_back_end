export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsCity = students.filter((student) => student.location === city);

  return studentsCity.map((student) => {
    const studentsGrade = newGrades.find(
      (grade) => grade.studentId === student.id,
    );
    if (studentsGrade) {
      return { ...student, grade: studentsGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });
}
