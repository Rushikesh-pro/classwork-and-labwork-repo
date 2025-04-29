def rev_list(l):
    return l[::-1]

l=[34,98,45,67,88]

ans=(rev_list(l))
print("the Reverse of a given list is",ans)


l1 = [89,67,76,67]
remove_dup=list(set(l1))
print("The final list is ",remove_dup)
print(remove_dup)

sorted_list=sorted(remove_dup)
print(sorted_list)

print("The sorted element in a list ",sorted_list)

second_largest=sorted_list[-2]
print("The second largest number is ",second_largest)