import random

def generate_code():
    # 定义一个种子，从这里面随机拿出一个值，可以是字母
    seeds = "1234567890"
    # 定义一个空列表，每次循环，将拿到的值，加入列表
    random_num = []
    # choice函数：每次从seeds拿一个值，加入列表
    for i in range(4):
        random_num.append(random.choice(seeds))
    # 将列表里的值，变成四位字符串
    return "" . join(random_num)


# if __name__ == '__main__':
#     print(generate_code())

