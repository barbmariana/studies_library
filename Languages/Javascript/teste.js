const estudantes = require("./teste.json");

for(let [chave, valor] of Object.entries(estudantes))
{
    console.log(chave + " :" + JSON.stringify(valor));
}

