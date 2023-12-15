function func(){
    let check = document.getElementById("visible")
    let passwords = document.getElementsByClassName("password")
    if (check.checked){
        passwords[0].setAttribute("type", "text")
        passwords[1].setAttribute("type", "text")
    }
    else{
        passwords[0].setAttribute("type", "password")
        passwords[1].setAttribute("type", "password")
    }
}

