from array import array

arr =array('i',[1,2,3,4,5,6,7,8,9])
print(arr)

#Updating the array
arr[2]=10
print(arr)

#Append the value to array
arr.append(15)
print(arr)

#Inserting an element
arr.insert(2,15)
print(arr)

#Deleting an element from an array using remove() & pop()
arr.remove(15)
print(arr)
arr.pop(0)
print(arr)

