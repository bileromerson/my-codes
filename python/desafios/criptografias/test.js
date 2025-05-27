var key = 'dredwdd' 
const text = 'dredwddfreffffffffffffffffffff'
              dredwdddredwdddredwdddredwddd
for (let tamanhokey = key.length; tamanhokey < text.length;) {
  key += key;
  tamanhokey = key.length;
  console.log(key)
}
for (let tamanhokey = key.length; tamanhokey > text.length;) {
  key = key.slice(0, -1);
  tamanhokey = key.length;
  console.log(key)
}

