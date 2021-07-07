counter =100    #int
miles=100.0     #float
name ="John"    #String
o_nu=0o10       #octal but base is int
hx_nu=0x10      #hexadecimal but base is int    
bi_nu=0b10      #binary but base is int
cmplx_nu=2+3j   #complex add j to the imaginary part to make it complex
f_ex=1.79e308   #floating (exponential form)
b_t=True
b_f=False
print(type(counter))
print(type(miles))
print(type(name))
print(type(o_nu))
print(type(hx_nu))
print(type(bi_nu))
print(type(cmplx_nu))
print(type(f_ex))
print(type(b_t))
print(type(b_f))

#implicit Conversion

num_int=120
# print("implicit conversion of int (l.d) to float(h.d): ",type(num_int+1.0),"output: ",num_int+1.0)

num_int=123
num_str="456"
# print("implicit conversion trial with string and int ",type(num_int+num_str),"output: ",num_int+num_str)

#To tackle this we have explicit data conversion
# predefined functions to use int(), float(), str()

print(num_int+int(num_str)) # 579 int type
print(str(num_int)+num_str) #123456 str type

