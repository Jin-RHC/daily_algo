sentence = input().strip()
list_sentence = list(sentence) # 문장을 리스트화
lst = [] # 괄호의 쌍들을 저장하는 리스트
stack = [] # 괄호 검사를 위한 임시 스택
for idx, value in enumerate(list_sentence):
    if value == '(':
        stack.append(['(', idx])
    elif value == ')':
        temp = stack.pop()
        lst.append([temp[1], idx])

result = set() # 결과 저장을 위한 리스트
lst_length = len(lst)
for i in range(1, 2 ** lst_length):
    target = list_sentence[:]
    case = []
    for j in range(lst_length):
        if i & 1 << j:
            case += lst[j]
    for k in case:
        target[k] = ''
    result.add(''.join(target))

result = list(result)
result.sort()
for i in result:
    print(i)