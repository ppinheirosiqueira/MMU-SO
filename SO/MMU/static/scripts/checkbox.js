document.addEventListener('DOMContentLoaded', function () {
    var elementos = document.getElementsByClassName('algoritmo')

    for(let item of elementos){
        item.addEventListener('change', function (){
            if (item.checked){
                for (let item of elementos){
                    if (item.checked == false){
                        return
                    }
                }
                document.querySelector('#todos').checked = true
            }
            else{
                document.querySelector('#todos').checked = false
            }
        })
    }
})

function setCheckboxAlgoritmos() {
    var todos = document.querySelector('#todos')
    var elementos = document.getElementsByClassName('algoritmo')

    if(todos.checked) {
        for(let item of elementos){
            item.checked = true
        }
    } else {
        for(let item of elementos){
            item.checked = false
        }
    }
}