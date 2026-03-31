def reverseWords(input):
    inputWords = input.split(" ")
    print(inputWords)
    # 一共有三个参数
    # 第一个参数-1表示从最后一个元素开始
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1表示每次向前移动一位
    outputWords = inputWords[-1::-1]
    return outputWords


if __name__ == "__main__":
    input = input("请输入一句话：")
    output = reverseWords(input)
    print(output)