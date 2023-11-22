document.addEventListener('DOMContentLoaded', function () {
    const jsonFileInput = document.getElementById('jsonFileInput')
    const importJsonButton = document.getElementById('importJsonButton')

    importJsonButton.addEventListener('click', function () {
        jsonFileInput.click()
    });

    jsonFileInput.addEventListener('change', function () {
        const selectedFile = jsonFileInput.files[0]
        if (selectedFile) {
            processJsonFile(selectedFile)
        }
    });
})

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function processJsonFile(file) {
    const formData = new FormData()
    formData.append('json_file', file)

    fetch('process_json/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message)
        } else {
            alert('Erro ao processar o arquivo JSON.')
        }
    })
    .catch(error => {
        console.error('Erro na solicitação:', error)
    })
}