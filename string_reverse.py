def reverse_string(n):
    word = ''
    for i in range(n):
        word = word + str(i)+" "
    return word

sen = reverse_string(1000)[::-1]
print(sen)