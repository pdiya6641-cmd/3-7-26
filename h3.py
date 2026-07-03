mobile = [2, 5, 8, 12]
counter = [1, 3, 7, 10, 15]

merged = []

i = 0
j = 0

while i < len(mobile) and j < len(counter):
    if mobile[i] < counter[j]:
        merged.append(mobile[i])
        i += 1
    else:
        merged.append(counter[j])
        j += 1

while i < len(mobile):
    merged.append(mobile[i])
    i += 1

while j < len(counter):
    merged.append(counter[j])
    j += 1

print("Final Waitlist:", merged)