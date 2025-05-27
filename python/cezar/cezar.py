
def criptografar(mensagem, deslocamento):
    resultado = ""
    for char in mensagem:
        if char.isalpha():  # Verifica se é uma letra
            base = ord('a') if char.islower() else ord('A')
            # Calcula a nova posição com o deslocamento
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char  # Mantém caracteres não alfabéticos
    return resultado

# Inputs do usuário
mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite o deslocamento: "))

# Criptografia
mensagem_criptografada = criptografar(mensagem, deslocamento)
print("Mensagem criptografada:", mensagem_criptografada)

# Descriptografia
mensagem_descriptografada = criptografar(mensagem_criptografada, -deslocamento)
print("Mensagem descriptografada:", mensagem_descriptografada)
