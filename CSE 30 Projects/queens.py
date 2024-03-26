def solve_queens(n):
    def is_valid_solution(solution):
        for num1 in range(n):
            for num2 in range(num1 + 1, n):
                if abs(solution[num1] - solution[num2]) == num2 - num1:
                    return False
        return True

    solutions = []
    for perm in all_perms(range(n)):
        if is_valid_solution(perm):
            solutions.append(perm)
    return solutions

def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

if __name__ == '__main__':
    data = [1,2,3,4]
    for i in all_perms(data):
        print(i)

if __name__ == '__main__':
    n = int(input('Enter a number of queens: \n'))
    solutions = solve_queens(n)
    print(f'The {n}-queens puzzle has {len(solutions)} solutions:')
    for solution in solutions:
        print (solution)