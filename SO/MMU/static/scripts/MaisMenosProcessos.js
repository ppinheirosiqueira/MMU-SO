function adicionarLinhaProcesso() {
    // Cria um novo conjunto
    var divProcessos = document.querySelector('.processos')
    var qtdConjuntosProcessos = document.querySelectorAll('.inputProcesso').length
    var novoProcesso = document.createElement('div')
    novoProcesso.className = 'inputProcesso'
    novoProcesso.innerHTML = `
        <hr>
        <label for="qtdPro${qtdConjuntosProcessos + 1}">Quantidade de processos:</label>
        <input type="number" name="qtdPro${qtdConjuntosProcessos + 1}" class="qtdPro${qtdConjuntosProcessos + 1}">
        <label for="tamPro${qtdConjuntosProcessos + 1}">Tamanho do Processo (nº de páginas):</label>
        <input type="number" name="tamPro${qtdConjuntosProcessos + 1}" class="tamPro${qtdConjuntosProcessos + 1}">
    `

    // Adiciona o novo conjunto ao container
    divProcessos.appendChild(novoProcesso)

    if (qtdConjuntosProcessos == 1) {
        var menosButton = document.querySelector('#menosProcesso')
        menosButton.style.display = 'inline'
    }
}

function removerLinhaProcesso() {
    // Obtém todos os conjuntos de inputs
    var conjuntosProcessos = document.querySelectorAll('.inputProcesso')

    // Garante que haja pelo menos um conjunto
    if (conjuntosProcessos.length > 1) {
        // Remove o último conjunto
        conjuntosProcessos[conjuntosProcessos.length - 1].remove()
    }
    
    if (conjuntosProcessos.length == 2) {
        var menosButton = document.querySelector('#menosProcesso')
        menosButton.style.display = 'none'
    }
}

function adicionarLinhaProcesso() {
    // Cria um novo conjunto
    var divProcessos = document.querySelector('.processos')
    var qtdConjuntosProcessos = document.querySelectorAll('.inputProcesso').length
    var novoProcesso = document.createElement('div')
    novoProcesso.className = 'inputProcesso'
    novoProcesso.innerHTML = `
        <hr>
        <label for="qtdPro${qtdConjuntosProcessos + 1}">Quantidade de processos:</label>
        <input type="number" name="qtdPro${qtdConjuntosProcessos + 1}" class="qtdPro${qtdConjuntosProcessos + 1}">
        <label for="tamPro${qtdConjuntosProcessos + 1}">Tamanho do Processo (nº de páginas):</label>
        <input type="number" name="tamPro${qtdConjuntosProcessos + 1}" class="tamPro${qtdConjuntosProcessos + 1}">
    `

    // Adiciona o novo conjunto ao container
    divProcessos.appendChild(novoProcesso)

    if (qtdConjuntosProcessos == 1) {
        var menosButton = document.querySelector('#menosProcesso')
        menosButton.style.display = 'inline'
    }
}

function removerLinhaProcesso() {
    // Obtém todos os conjuntos de inputs
    var conjuntosProcessos = document.querySelectorAll('.inputProcesso')

    // Garante que haja pelo menos um conjunto
    if (conjuntosProcessos.length > 1) {
        // Remove o último conjunto
        conjuntosProcessos[conjuntosProcessos.length - 1].remove()
    }
    
    if (conjuntosProcessos.length == 2) {
        var menosButton = document.querySelector('#menosProcesso')
        menosButton.style.display = 'none'
    }
}

function adicionarLinhaProcesso() {
    // Cria um novo conjunto
    var divProcessos = document.querySelector('.processos')
    var qtdConjuntosProcessos = document.querySelectorAll('.inputProcesso').length
    var novoProcesso = document.createElement('div')
    novoProcesso.className = 'inputProcesso'
    novoProcesso.innerHTML = `
        <hr>
        <label for="qtdPro${qtdConjuntosProcessos + 1}">Quantidade de processos:</label>
        <input type="number" name="qtdPro${qtdConjuntosProcessos + 1}" class="qtdPro${qtdConjuntosProcessos + 1}">
        <label for="tamPro${qtdConjuntosProcessos + 1}">Tamanho do Processo (nº de páginas):</label>
        <input type="number" name="tamPro${qtdConjuntosProcessos + 1}" class="tamPro${qtdConjuntosProcessos + 1}">
    `

    // Adiciona o novo conjunto ao container
    divProcessos.appendChild(novoProcesso)

    if (qtdConjuntosProcessos == 1) {
        var menosButton = document.querySelector('#menosProcesso')
        menosButton.style.display = 'inline'
    }
}

function removerLinhaProcesso() {
    // Obtém todos os conjuntos de inputs
    var conjuntosProcessos = document.querySelectorAll('.inputProcesso')

    // Garante que haja pelo menos um conjunto
    if (conjuntosProcessos.length > 1) {
        // Remove o último conjunto
        conjuntosProcessos[conjuntosProcessos.length - 1].remove()
    }
    
    if (conjuntosProcessos.length == 2) {
        var menosButton = document.querySelector('#menosProcesso')
        menosButton.style.display = 'none'
    }
}

function adicionarLinhaMemoria() {
    // Cria um novo conjunto
    var divMemoria = document.querySelector('.memoria')
    var qtdConjuntosMemoria = document.querySelectorAll('.inputMemoria').length
    var novoMemoria = document.createElement('div')
    novoMemoria.className = 'inputMemoria'
    novoMemoria.innerHTML = `
        <hr>
        <label for="X${qtdConjuntosMemoria + 1}">Tamanho da memória RAM (relativo a SWAP):
        </label><input type="number" name="X${qtdConjuntosMemoria + 1}" id="X${qtdConjuntosMemoria + 1}" value=10 min="1" max="100">
    `

    // Adiciona o novo conjunto ao container
    divMemoria.appendChild(novoMemoria)

    if (qtdConjuntosMemoria == 1) {
        var menosButton = document.querySelector('#menosMemoria')
        menosButton.style.display = 'inline'
    }
}

function removerLinhaMemoria() {
    // Obtém todos os conjuntos de inputs
    var conjuntosMemoria = document.querySelectorAll('.inputMemoria')

    // Garante que haja pelo menos um conjunto
    if (conjuntosMemoria.length > 1) {
        // Remove o último conjunto
        conjuntosMemoria[conjuntosMemoria.length - 1].remove()
    }
    
    if (conjuntosMemoria.length == 2) {
        var menosButton = document.querySelector('#menosMemoria')
        menosButton.style.display = 'none'
    }
}

function setListaProcessos() {
    var aleatorio = document.querySelector('#aleatorio')
    var elementos = document.getElementsByClassName("listaProcessos")

    if(aleatorio.checked) {
        for(let item of elementos){
            item.style.display = 'none'
        }
    } else {
        for(let item of elementos){
            item.style.display = 'block'
        }
    }
}