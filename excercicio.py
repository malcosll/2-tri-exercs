class Cliente:
    def __init__(self,nome,idade,sexo,email,telefone,endereco,):
     self.nome = nome
     self.idade = idade
     self.sexo = sexo
     self.email = email
     self.telefone = telefone
     self.endereco = endereco

 
    def __str__(self):
       return f'{self.nome} - {self.idade} - {self.sexo} - {self.email} - {self.telefone} - {self.endereco}'
    
marcos = Cliente ("Marcos",17,"Masculino","Marcos@gmail.com",(41)9999-9999,"R.Marcos")

print(marcos)