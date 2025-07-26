import ast

def combine_elements(list1, list2):
    merged = list1 + list2
    merged.sort(key=lambda x: x["positions"][0])  
    result = []
    used = [False] * len(merged)

    for i in range(len(merged)):
        if used[i]:
            continue
        current = merged[i]
        c_left, c_right = current["positions"]
        c_values = current["values"]

        for j in range(i + 1, len(merged)):
            if used[j]:
                continue
            other = merged[j]
            o_left, o_right = other["positions"]

          
            overlap = min(c_right, o_right) - max(c_left, o_left)
            if overlap > 0:
                o_width = o_right - o_left
                if overlap >= 0.5 * o_width:
                   
                    c_values += other["values"]
                    used[j] = True

        result.append({
            "positions": [c_left, c_right],
            "values": c_values
        })
        used[i] = True

    return result


print("Enter list1:")
list1 = ast.literal_eval(input())  

print("Enter list2:")
list2 = ast.literal_eval(input())


output = combine_elements(list1, list2)
print("\nMerged Output:")
for item in output:
    print(item)
