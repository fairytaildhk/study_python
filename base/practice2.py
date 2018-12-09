if __name__ == '__main__':
    user = {"name": "Lili",
            "age": "18",
            "city": "shanghai",
            "first_name": "Li",
            "last_name": "li",
            "name2": "Lili",
            }
    # 遍历字典
    for k, v in user.items():
        print(k + ":" + v)
    # 遍历key
    print("第一种遍历字典key")
    for k in user.keys():
        print(k)
    print("第二种遍历字典key")
    for k in user:
        print(k)
    # 遍历value
    print("遍历字典获取value")
    for v in user.values():
        print(v)
    # 去重
    print("去除重复")
    for v in set(user.values()):
        print(v)
    # 修改字典
    user['age'] = '20'
    print(user)
    # 删除键值对
    del user['city']
    print(user)
    # 添加
    user['new'] = 'abc'
    print(user)
    user['new1'] = 'abc'
    print(user)

    number = [3, 34, 5, 255, 62, 22]
    print(sorted(number))
