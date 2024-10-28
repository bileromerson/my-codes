from PIL import Image

tentativas = 0
quantidade = int(input("quantidade: \n - "))
imagem = Image.open("my-codes\leg de imagem\img.jpg")

while tentativas <= quantidade -1:
    imagem.show()
    tentativas +=1
