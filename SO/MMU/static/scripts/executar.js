async function fetchData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    } catch (error) {
        throw error;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('MMUForm')

    formulario.addEventListener('submit', async function (event) {
        event.preventDefault() // Evita o envio padrão do formulário

        const vetorQtdPro = []
        const vetorTamPro = []

        // Itera sobre os elementos do formulário
        for (const elemento of formulario.elements) {
            if (elemento.name.startsWith('qtdPro') && elemento.name.slice(6).match(/^\d+$/)) {
                const numeroProcesso = elemento.name.slice(6)
                vetorQtdPro.push(elemento.value)

                // Construa o nome do campo "tamPro" correspondente
                const nomeCampoTamPro = 'tamPro' + numeroProcesso

                // Encontre o elemento correspondente ao campo "tamPro"
                const elementoTamPro = formulario.elements[nomeCampoTamPro]

                if (elementoTamPro) {
                    vetorTamPro.push(elementoTamPro.value)
                }
            }
        }

        const urlSWAP = `/criarSwap/${JSON.stringify(vetorQtdPro)}/${JSON.stringify(vetorTamPro)}`

        try {
            const dataSWAP = await fetchData(urlSWAP)
            console.log("SWAP criada com sucesso")
        } catch (error) {
            console.log('Ocorreu um erro:', error);
        }

        aleatorio = document.getElementById('aleatorio').checked? 1 : 0
        lote = document.getElementById('Lote').checked? 1 : 0
        qtdProExe = document.getElementById('qtdProExe').value
        listaProcessos = document.getElementById('lista').value.split(',')

        if (!aleatorio && listaProcessos == ''){
            alert('A Lista de Processos não pode ser vazia ao desligar o aleatório')
            return
        }

        const urlLP = `/criarListaProcessos/${aleatorio}/${lote}/${qtdProExe}/${JSON.stringify(listaProcessos)}`

        try {
            const dataLP = await fetchData(urlLP)

            if (dataLP['status'] !== "Sucesso") {
                alert(dataLP['status'])
                return
            }
        } catch (error) {
            console.log('Ocorreu um erro:', error)
        }

        formulario.submit()
    })
})
