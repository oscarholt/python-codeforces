def main():
    problem_count = int(input())
    sure_count = 0

    for i in range(problem_count):
        is_sure = input().split()
        sure_1 = int(is_sure[0])
        sure_2 = int(is_sure[1])
        sure_3 = int(is_sure[2])
        if sure_1 + sure_2 + sure_3 >= 2:
            sure_count += 1

    print(sure_count)
    return

main()

