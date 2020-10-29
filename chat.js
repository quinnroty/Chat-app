function requestChat() {
    ajaxGetRequest("/chat", renderChat);
}

function renderChat(jsonData){
    let messages = JSON.parse(jsonData)
    console.log(messages)
    let chat = "";
    for(let data of messages){
        chat = chat + data.message + "</br>";
    }
    let chatElem = document.getElementById("chat");
    chatElem.innerHTML = chat;
}

function sendMessage(){
    let messageElement = document.getElementById("message");
    
    let message = messageElement.value;
    messageElement.value = "";
    let toSend = JSON.stringify({"message": message});

    ajaxPostRequest("/send", toSend, renderChat);
}


function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}


function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}