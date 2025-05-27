from PIL import Image

tentativas = 1
quantidade = int(input("quantidade: \n - "))
imagem = Image.open("leg de imagem\img.jpg")

while tentativas <= quantidade:
    tentativas +=1
    imagem.show()
