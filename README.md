Learning Basic Algorithms

---




**Tips:**

Read till EOF (for UVA 😫):
```python
# Python 3
while True:
    try:
        s = input()
        # do something
    except EOFError:
        break
```

Đặc biệt, các bài **_Disjoint Set Union_** của UVA thì dùng template sau đọc input:

```python
# Python 3
line = input()
while line != '':
    # do something

    try:
        line = input()
    except EOFError:
        break
```