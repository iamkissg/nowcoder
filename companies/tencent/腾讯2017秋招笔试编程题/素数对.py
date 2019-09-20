# __author__ = 'iamkissg'
# __date__ = 20190920



def generate_prime_numbers(max_num):
    prime_nums = []
    nums = [0] * max_num

    for i in range(2, max_num):
        if nums[i]:
            continue
        else:
            prime_nums.append(i)
            cur_num = 2 * i
            while cur_num < max_num:
                nums[cur_num] = 1
                cur_num += i
    return prime_nums
            
prime_nums = generate_prime_numbers(1000)

target = int(input())
p1, p2 = 0, len(prime_nums)-1

result = []
while p1 <= p2:
    s = prime_nums[p1] + prime_nums[p2]
    if s < target:
        p1 += 1
    elif s > target:
        p2 -= 1
    else:
        result.append((p1, p2))
        p1 += 1
        p2 -= 1
print(len(result))