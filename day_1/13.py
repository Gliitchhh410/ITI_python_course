true_example = [1,2,3,4]
false_example = [1,1,2,3,4,4,5,6,7]


def is_different(example):
    if len(example) == len(set(example)):
        return True
    else:
        return False

print(is_different(true_example))
print(is_different(false_example))