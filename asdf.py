K = int(input())
account_book = None

for i in range(K):
	Input = int(input())
    if Input == 0:
        account_book.pop()
    else:
        account_book.append(Input)
