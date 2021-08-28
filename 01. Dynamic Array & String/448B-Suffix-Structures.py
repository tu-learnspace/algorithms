"""
https://codeforces.com/problemset/problem/448/B

- Có các phép biến đổi
- Automaton: xóa bất kỳ
- Array: đổi chỗ 2 ký tự
- Nếu cần cả 2 thì là both
- Nếu ko thể thì là need tree

- Input:
    + dòng 1: xâu s
    + dòng 2: xâu t
- Output:
    + in ra phương pháp cần
IDEA:
- Các TH:
    + Nếu 1 ký tự có trong t mà ko có trong s  -> Need tree
    + Nếu 1 ký tự có trong s mà ko có trong t -> automaton xóa ký tự
    + Thứ tự xuất hiện không khớp -> array
    + Cả 2 cái trên -> both
- Đếm tần suất các kí tự trong s và t -> giải quyết đc need tree & automaton
- giải quyết array: c1: có thể sort 2 chuỗi rồi so sánh độ dài, có trùng nhau ko, nếu = nhau là array
- c2:

"""

s = input()
t = input()

need_tree = array = automaton = False
# frequency
for i in range(26):  # 26 ky tu trong alphabet
    cnt_s = s.count(chr(i + ord('a')))
    cnt_t = t.count(chr(i + ord('a')))

    if cnt_t < cnt_s:
        automaton = True
    elif cnt_t > cnt_s:
        need_tree = True

index_found, match = 0, -1

for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        array = True
        break

if need_tree:
    print("need tree")
elif automaton and array:
    print("both")
elif automaton:
    print("automaton")
else:
    print("array")