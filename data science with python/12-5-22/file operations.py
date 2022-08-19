file_ob=open("f1.text","w")
print("file created")
print("file append")
file_ob.write("hello....")
file_ob.write("welcome \n python \n rgukt")
file_ob.close()
print("end of the file")



file_ob=open("f2.txt","w")
text=file_ob.readlines()
print("text")
file_ob.close()
print("end of the file")
