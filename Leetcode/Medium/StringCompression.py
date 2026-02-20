def StringCompression(chars):
    n = len(chars)
    read = 0 
    write = 0 

    while read < n:
        current_char = chars[read]
        count = 0

        # count consecutive occurences of the current character

        while read < n and chars[read] == current_char:
            read += 1
            count += 1
        
        chars[write] = current_char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
            
    return write 

chars = ["a","a","b","b","c","c","c"]
length = StringCompression(chars)
print(length)
chars = ["a"]
length = StringCompression(chars)
print(length)
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","b"]
length = StringCompression(chars)
print(length)
