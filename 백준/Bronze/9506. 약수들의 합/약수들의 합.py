def is_perfect(num):
    if num == -1:
        return

    res = [i for i in range(1, num // 2 + 1) if num % i == 0]
    if sum(res) == num:
        print(f"{num} = " + " + ".join(map(str, res)))
    else:
        print(f"{num} is NOT perfect.")

while True:
    num = int(input())
    if num == -1:
        break
    is_perfect(num)