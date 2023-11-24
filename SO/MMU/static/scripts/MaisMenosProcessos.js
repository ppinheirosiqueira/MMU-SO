function adicionarLinha() {
    // Cria um novo conjunto
    var divProcessos = document.querySelector('.processos')
    var qtdConjuntosProcessos = document.querySelectorAll('.inputProcesso').length
    var novoProcesso = document.createElement('div')
    novoProcesso.className = 'inputProcesso'
    novoProcesso.innerHTML = `
        <label for="qtdPro${qtdConjuntosProcessos + 1}">Quantidade de processos:</label>
        <input type="number" name="qtdPro${qtdConjuntosProcessos + 1}" class="qtdPro${qtdConjuntosProcessos + 1}">
        <label for="tamPro${qtdConjuntosProcessos + 1}">Tamanho do Processo (nº de páginas):</label>
        <input type="number" name="tamPro${qtdConjuntosProcessos + 1}" class="tamPro${qtdConjuntosProcessos + 1}">
    `

    // Adiciona o novo conjunto ao container
    divProcessos.appendChild(novoProcesso)
}

function removerLinha() {
    // Obtém todos os conjuntos de inputs
    var conjuntosProcessos = document.querySelectorAll('.inputProcesso')

    // Garante que haja pelo menos um conjunto
    if (conjuntosProcessos.length > 1) {
        // Remove o último conjunto
        conjuntosProcessos[conjuntosProcessos.length - 1].remove()
    }
}