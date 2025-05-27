function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var chatWindow = document.getElementById('chat-window');

    if (messageInput.value.trim() !== '') {
        var newMessage = document.createElement('div');
        newMessage.className = 'message';
        newMessage.textContent = messageInput.value;

        chatWindow.appendChild(newMessage);

        // Limpar o campo de entrada
        messageInput.value = '';

        // Rolagem automática para a última mensagem
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}