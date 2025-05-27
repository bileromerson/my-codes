

text = 'senha: Enzo3375'; // input
const bits = text.split('').map(char => char.charCodeAt().toString(2).padStart(8, '0')).join('');
const tamanho = bits.length;



const encription = () => {
    let key ='';
    let encText = '';
    
    for(let i=0; i<tamanho; i++){
        key += Math.random() < 0.5 ? 0 : 1;
        console.log(key);
    }
    console.log('----------------------------------------------------------');
    for(let j=0; j<tamanho; j++){
        if (key[j] == 1) {
            encText += bits[j] == 1 ? 0 : 1;
        } else {
            encText += bits[j];
        }
    }
    let resultadobin = encText.match(/.{1,8}/g).join(' ');
    let resultado = encText.match(/.{1,8}/g).map(byte => String.fromCharCode(parseInt(byte, 2))).join(''); 
    
    console.log('key: ............ ', key);
    console.log('mensage: ........ ',bits);
    console.log('encripted Text: . ', encText);  
    console.log('resultado: ', resultado);

    return resultado;

}
encription();