def read_file(filename):
    with open(filename, 'r',encoding='utf-8' ) as f:
        numbers = list(map(int, f.read().split()[2:]))
    return numbers

def find_shortest_subsequence(numbers):
    from collections import defaultdict

    left = 0
    count = defaultdict(int)
    unique_numbers = 0
    shortest = len(numbers) + 1 
    for right in range(len(numbers)):
        num = numbers[right]
        if count[num] == 0:
            unique_numbers += 1
        count[num] += 1

        while unique_numbers == 26:
            current_length = right - left + 1
            if current_length < shortest:
                shortest = current_length

            old_num = numbers[left]
            count[old_num] -= 1
            if count[old_num] == 0:
                unique_numbers -= 1
            left += 1

    if shortest <= len(numbers):
        return shortest
    else:
        return "NONE"

numbers = read_file('data_prog_contest_problem_2.txt')
print(find_shortest_subsequence(numbers))
