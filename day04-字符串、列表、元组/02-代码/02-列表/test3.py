
total_money = eval(input(''))
country = input('')
country_list = [0.21, 4.90, 0.65]
if country == 'Singapore':
    print(total_money*country_list[0])
elif country == 'Thailand':
    print(total_money*country_list[1])
elif country == 'Malaysia':
    print(total_money*country_list[2])
else:
    print('error')

#include<stdio.h>
# int main(){
#     printf("hello world")
#     return 0;
# }
#
# public class Main {
#     public static void main(){
#     System.out.println("hello world");
# }
# }
#
# print("hello world")