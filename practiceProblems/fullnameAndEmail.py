# Fullname and Email
# site: https://edabit.com/challenge/gB7nt6WzZy8TymCah
# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
#
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a "." in between, and follow it with '@company.com'
# at the end. Make sure everything is in lowercase.


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname.lower()
        self.lastname = lastname.lower()
        self.fullname = self.firstname + " " + self.lastname
        self.email = self.firstname + "." + self.lastname + "@company.com"

    # full name
    def fullname(self):
        print(self.firstname + " " + self.lastname)

    # email
    def email(self):
        print(self.firstname + "." + self.lastname + "@company.com")


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)
