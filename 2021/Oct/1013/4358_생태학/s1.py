import sys
sys.stdin = open('input.txt')

tree_dict = {}
tree_set = set()
cnt = 0

while True:
    tree = sys.stdin.readline().strip()
    if tree:
        tree_dict[tree] = tree_dict.get(tree, 0) + 1
        cnt += 1

    else:
        break

lst = sorted(list(tree_dict.keys()))
for i in lst:
    print('{} {:.4f}'.format(i, tree_dict[i]/cnt * 100))