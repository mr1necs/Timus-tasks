from math import sqrt


def find_min_squares(num, sum_sq):
    if sum_sq == 1:
        if sqrt(num) == int(sqrt(num)):
            return [int(sqrt(num))]
        return False
    for j in range(1, int(sqrt(num) + 1)):
        x = find_min_squares(num - j ** 2, sum_sq - 1)
        if x:
            return [j] + x
    return False


if __name__ == "__main__":
    n = int(input())
    mod = n % 4 if n % 4 != 0 else 1
    for i in range(mod, 5):
        sq = (find_min_squares(n, i))
        if sq:
            print(len(sq))
            break
