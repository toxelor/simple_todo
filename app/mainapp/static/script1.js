function func(){
    let check = document.getElementById("visible")
    let passwords = document.getElementsByClassName("password")
    if (check.checked){
        passwords[0].setAttribute("type", "text")
    }
    else{
        passwords[0].setAttribute("type", "password")
    }
    let toDelete = document.getElementById("error")
    if (toDelete != null){
        let parent = toDelete.parentNode
        parent.removeChild(toDelete)
    }
}


