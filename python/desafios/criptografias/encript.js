
var enc = []; // array para armazenar os valores encriptados

const encript = (enc) => { 
    const key = 20; // chave de criptografia (enc)
    const text = 'Hello World!'; // input
    for (let i = 0; i < text.length; i++) {
        let strText = text.charCodeAt(i) + key; // converte o caractere para o código ASCII e adiciona a chave
        let encripted = strText.toString(2).padStart(8, '0'); // converte o código ASCII para binário e preenche com zeros 
        let encriptedText = String.fromCharCode(strText); // converte o código ASCII de volta para o caractere
        enc.push(encripted); // armazena o valor encriptado no array
        console.log(strText, '---->', encripted, '---->', encriptedText.replace(/[^\x20-\x7E]/g, '??')); // mostra o processo de criptografia e substitui caracteres não imprimíveis por "??"
    }
    console.log('resultado:', enc.join(' - ')); // exibe o resultado final da criptografia com o " - " entre os valores
    return enc;
}

encript(enc);

console.log('----------------------------------------------------------');

const decript = (enc) => {
    const key = 20; // chave de criptografia (dec)
    var resultado = ''; // variável para armazenar o resultado da descriptografia
    for (let i = 0; i < enc.length; i++) {
        let strText = parseInt(enc[i], 2); // converte o valor binário de volta para ASCII
        let decriptedstr = strText - key; // subtrai a chave para obter o valor original
        let decriptedText = String.fromCharCode(decriptedstr); // converte o código ASCII de volta para o caractere
        console.log( strText, '---->', decriptedstr, '---->', decriptedText); // mostra o processo de descriptografia
        resultado += decriptedText; // armazena o caractere descriptografado no resultado
    }
    console.log('resultado: ', resultado); // exibe o resultado final da descriptografia
    return resultado;
}

decript(enc);