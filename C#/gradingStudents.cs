using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'gradingStudents' function below.
     *
     * HackerLand University has the following grading policy:
     * Every student receives a  in the inclusive range from  to .
     * Any  less than  is a failing grade.
     * Sam is a professor at the university and likes to round each
     * student's  according to these rules:
     *
     * If the difference between the  and the next multiple of  is less
     * than , round  up to the next multiple of .
     * If the value of  is less than , no rounding occurs as the result
     * will still be a failing grade.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY grades as parameter.
     */

    public static List<int> gradingStudents(List<int> grades)
    {
        List<int> finalGrades = new List<int>();
        for (int i = 0; i < grades.Count; i++) {
            int grade = grades[i];
            if ((grade % 5) > 2 && grade >= 38) {
                finalGrades.Add(grade + (5 - grade%5));
            } else {
                finalGrades.Add(grade);
            }
        }
        return finalGrades;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int gradesCount = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> grades = new List<int>();

        for (int i = 0; i < gradesCount; i++)
        {
            int gradesItem = Convert.ToInt32(Console.ReadLine().Trim());
            grades.Add(gradesItem);
        }

        List<int> result = Result.gradingStudents(grades);

        textWriter.WriteLine(String.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
