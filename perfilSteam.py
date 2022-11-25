class Profile:
    ##atributos##
    # username = ""
    # password = ""
    # email = ""
    ##fin atributos##   ##por ser python  de tipado dinamico se eliminan
    
    def __init__(self, username, id, email, password, level=0, status="online"):    ##__dunder##
        self.username = username
        self.id = id
        self.email = email
        self.password = password
        
    def print(self):
        print("nombre de usuario: "+ str(self.username))
        print("id: "+ self.id)
        print("email: "+ str(self.email))
        print("contraseña: "+ str(self.password))
