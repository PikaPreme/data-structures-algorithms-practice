# objects classes and inheritance practice

# self is the instance of the class


class Employee:

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def get_full_name(self):
        # return self.f_name, self.l_name
        return '{} {}'.format(self.f_name, self.l_name)

    def set_salary(self, new_salary):
        self.salary = new_salary


class Developer(Employee):

    def __init__(self, f_name, l_name, salary, prog_lang):
        super().__init__(f_name, l_name, salary)
        self.prog_lang = [prog_lang]

    def add_prog_lang(self, new_prog_lang):
        self.prog_lang += [new_prog_lang]


if __name__ == '__main__':
    bob = Employee('bob', 'smith', 100000)
    print(bob.get_full_name())
    bob.set_salary(150000)
    print(bob.salary)

    rich = Developer('richard', 'le', 100000, 'python')
    print(rich.salary)
    rich.set_salary(110000)
    print(rich.salary)
    print(rich.get_full_name())
    print(rich.prog_lang)
    rich.add_prog_lang('java')
    print(rich.prog_lang)
