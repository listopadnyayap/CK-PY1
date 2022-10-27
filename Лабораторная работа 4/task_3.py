def delete(list_, index=None):
    if index!=None:
        list_1=list_[:index]
        list_2=list_[index+1:]
        return list_1+list_2
    else:
        list_.pop(-1)
        return list_


print(delete([0, 0, 1, 2], index=0))  
print(delete([0, 1, 1, 2, 3], index=1))  
print(delete([0, 1, 2, 3, 4, 4]))  
