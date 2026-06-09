def split_string(example):
    output = []
    index = (len(example)+1) // 2
    output.append(example[:index])
    output.append(example[index:])
    return output

a_front, a_back = split_string('abcd')
print(a_front)
print(a_back)

b_front, b_back = split_string('xyz')
print(b_front)
print(b_back)

print("Final Output: ", a_front + b_front + a_back + b_back)