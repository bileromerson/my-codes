
const letrasMinusculas = "abcdefghijklmnopqrstuvwxyz";
const letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numeros = "0123456789";
const simbolos = "!@#$%&*";

var tamanhoSenha =  10; 
var incluirLetrasMinusculas = true;
var incluirLetrasMaiusculas = true;
var incluirNumeros = true;
var incluirSimbolos = true;
var senhaGerada = "";

const gerador = () => {
    for (var tamanho = 0; tamanho < tamanhoSenha;) {        

        if (incluirLetrasMinusculas) {
            senhaGerada += letrasMinusculas[Math.floor(Math.random() * letrasMinusculas.length)];
            tamanho++;
        }
        if (incluirLetrasMaiusculas) {
            senhaGerada += letrasMaiusculas[Math.floor(Math.random() * letrasMaiusculas.length)];
            tamanho++;
        }
        if (incluirNumeros) {
            senhaGerada += numeros[Math.floor(Math.random() * numeros.length)];
            tamanho++;
        }
        if (incluirSimbolos) {
            senhaGerada += simbolos[Math.floor(Math.random() * simbolos.length)];
            tamanho++;
        }
    }
    console.log(senhaGerada);
}
gerador();