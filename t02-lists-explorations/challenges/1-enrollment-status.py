"""_summary_
    Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
of the number of students, and the mean and median tuition values.
"""


def enrollment_stats(universities_lst: list) -> tuple:
    """Gathers and returns 2 separates with the total of students and tuitions by university"""

    total_students = []
    total_tuition = []

    for uni in universities_lst:
        total_students.append(uni[1])
        total_tuition.append(uni[2])

    return total_students, total_tuition


def mean(lst):
    """Calculates the mean from a list of values"""
    return sum(lst) / len(lst)


def testFunc():
    pass


def median(lst):
    """Calculates the median from a list of values"""
    lst.sort()
    if len(lst) % 2 == 0:
        lst_middle = len(lst) / 2
        middle_first, middle_second = lst_middle - 1, lst_middle
        return sum(middle_first, middle_second) / len(lst)

    return lst[len(lst) // 2]


if __name__ == "__main__":
    universities = [
        ["California Institute of Technology", 2175, 37704],
        ["Harvard", 19627, 39849],
        ["Massachusetts Institute of Technology", 10566, 40732],
        ["Princeton", 7802, 37000],
        ["Rice", 5879, 35551],
        ["Stanford", 19535, 40569],
        ["Yale", 11701, 40500],
    ]
    totals = enrollment_stats(universities)
    print("*" * 35)
    print(f"Total students:   {sum(totals[0]):,}")
    print(f"Total tuitions: $ {sum(totals[1]):,}")

    print(f"\nStudent Mean:     {mean(totals[0]):,.2f}")
    print(f"Student Median:   {median(totals[0]):,}")

    print(f"\nTuition Mean:   $ {mean(totals[1]):,.2f}")
    print(f"Tuition Median: $ {median(totals[1]):,}")
    print("*" * 35)
