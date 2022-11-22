from perfilSteam import Profile

# def ccontraseña ():
#     print("¿Desea cambiar la contraseña?")
#     option =int(input("(1)Si    (2)No \n"))
#     if (option == 1):
#         password = str(input("Ingrese su contraseña: "))
#         rePassword = str(input("Repita su contraseña: "))
        
#         profile1 = Profile(userName, id, email, password)
#         profile1.print()
def main():

    while(True):
        userName = str(input("Ingrese su nombre de usuario: "))    
        id = input("Ingrese su id: ")
        email = str(input("Ingrese su email: "))
        
        password = str(input("Ingrese su contraseña: "))
        rePassword = str(input("Repita su contraseña: "))
        
        if (password != rePassword):
            print("Las contraseñas no coinciden")
            continue
            
        profile1 = Profile(userName, id, email, password)

        profile1.print()
        while(True):
            print("¿Desea cambiar la contraseña?")
            option =int(input("(1)Si    (2)No \n"))
            if (option == 1):
                password = str(input("Ingrese su contraseña: "))
                rePassword = str(input("Repita su contraseña: "))
                
                profile1 = Profile(userName, id, email, password)
                profile1.print()
                
            elif (option ==2):
                break
            
            
        
        
main()
