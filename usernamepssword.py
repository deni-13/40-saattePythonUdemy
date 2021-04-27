print("""****************
user login


***************""")
sys_username="deniz"
sys_parola="2345"

usernme=input("username?:")
passwordd=input("password")

if sys_username==usernme and sys_parola==passwordd:
    print("succesful")

elif sys_username!=usernme and sys_parola==passwordd:
    print("Wrong username")

elif sys_username==usernme and sys_parola!=passwordd:
    print("wrong password")

else:
    print("Try again")