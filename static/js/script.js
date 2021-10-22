var corpo = window.document.body

function SiteClaro(){
    corpo.style.background="#fff"
    // Tags Restantes
    var resto = window.document.getElementsByClassName("ti")
    for(var grupoClasses = 0; grupoClasses<resto.length; grupoClasses+=1){
        resto[grupoClasses].style.color="#003153"
    }
}


function SiteEscuro(){
    corpo.style.background="#3B444B"
    // Cor Parágrafos.
    var paragrafos = window.document.getElementsByTagName("p")
    for(var c = 0; c<paragrafos.length; c+=1){
        if(c != 5 && c != 6 && c != 7){
            paragrafos[c].style.color="#fff"
        }
    }
    // Cor Títulos h1
    var titulosH1 = window.document.getElementsByTagName("h1")
    for(var t = 0; t<titulosH1.length; t+=1){
        if(t != 0 && t != 1 && t != 2){
            titulosH1[t].style.color="#fff"
        }
    }
    // Cor Títulos h2
    var titulosH2 = window.document.getElementsByTagName("h2")
    for(var s = 0; s<titulosH2.length; s+=1){
        titulosH2[s].style.color="#fff"
    }
    // Tags Restantes
    var resto = window.document.getElementsByClassName("ti")
    for(var grupoClasses = 0; grupoClasses<resto.length; grupoClasses+=1){
        resto[grupoClasses].style.color="#fff"
    }
    var rest = window.document.getElementsByClassName("tt")
    for(var Classes = 0; Classes<rest.length; Classes+=1){
        rest[Classes].style.color="#003153"
    }
}


// Condição que verifica se há alguma preferência já salva.
if(localStorage.tema){
    // Condição de cada tema.
    if(localStorage.tema == "escuro"){
        SiteEscuro()
    }
    else if(localStorage.tema == "claro"){
        SiteClaro()
    }
}


// Função pra salvar a preferência do usuário localmente.
function FuncTema(){
    // Pega o valor do select e salva no id tema.
    var tema = window.document.getElementById("tema").value
    localStorage.setItem("tema", tema)
    // Condição de cada tema.
    if(localStorage.tema == "escuro"){
        SiteEscuro()
    }
    else if(localStorage.tema == "claro"){
        SiteClaro()
    }
}

