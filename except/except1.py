'''
java
try{
    //예외가 의심되는 코드
}catch(FileNotFoundException e){
    //FilNotFoundException 처리하는 코드
}catch{
    //예외가 났을 때 처리하는 코드
}finally{
    //무조건 실행해야하는 코드
}
python
try:
    //예외가 의심되는 코드
except ValueError as e:
    #ValueError 처리하는 코드
except:
    #예외가 났을 때 처리하는 코드
finally:
    #무조건 실행해야하는 코드
'''
# print(int('안녕'))
# list1 = [1,2,3]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# print(list2)        #NameError: name 'list2' is not define
print(10/10)       #1.0
print(5/10)        #0.5
print(1/10)        #0.1
print(0/10)        #0? error?
print(10/5)        #2.0
print(10/1)        #10.0
print(10/0.1)      #100.0
print(10/0.01)    #1000.0
# print(10/0)     #ZeroDivisionError: division by zero
