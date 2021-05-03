class Test:

    def goal_replacer(stri):
        return (stri.replace('()','o').replace('(al)','al'))


if __name__ == '__main__':
    print(Test.goal_replacer("(al)G(al)()()G"))