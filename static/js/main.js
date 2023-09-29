
const python = `
import requests\n
transaction = {\n
\t#...data\n
}\n
data = {\n
\t"data": transaction\n
}\n
res = requests.post(url,data=data)\n
print(res.text)\n
`

const node = `
const axios = require('axios');\n
const transaction = {\n
\t//..data
}\n
const data = {\n
\tdata: transaction
}\n
async function call(){\n
\tconst res = await axios.post(url,data);\n
\tconsole.log(res.data);\n
}\n
call();\n
`

const codes = {
    node,
    python
}



const btns = document.querySelectorAll('.language-btns');
const title = document.getElementById('title');
var htmlCodeInstance = CodeMirror(document.getElementById("html-box"), {
    lineNumbers: true,
    tabSize: 4,
    mode: "python",
    theme: "ayu-mirage",
    styleActiveLine: true,
    autoCloseTags: true,
    autoCloseBrackets: true,
    value: python
});

let language = 'python'
btns.forEach(ele => {
    ele.addEventListener('click',function(){
        const datavalue = ele.dataset.language;
        title.innerText = datavalue[0].toLocaleUpperCase()+datavalue.slice(1,datavalue.length);
        
        if (datavalue?.toLowerCase() === 'node'){
            language = 'javascript';
            htmlCodeInstance.setOption('mode','javascript')
        }else{
            language = datavalue;
            htmlCodeInstance.setOption('mode',datavalue)
        }

        htmlCodeInstance.setValue(codes[datavalue]);

    });
})
