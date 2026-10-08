async function sendCommand(flask, periodMS){
    var response = await fetch(`/api/${flask}/${periodMS}`);
    var replyText = await response.text();
    
    console.log(replyText)
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText
}

function main() {
    console.log("Hello JavaScript!");
    document.querySelector('#on').onclick = () => {
        console.log("You pressed the ON button!");
        //sendCommand("RESET");
    };
    document.querySelector('#off').onclick = () => {
        console.log("You pressed the OFF button!");
        //sendCommand("RESET");
    };
    
    document.querySelector('#flash').onclick = () => {
        let flashes = document.querySelector("#flashes").value;
        let periodMS = document.querySelector("#periodMS").value;
        console.log("FLASH!");
        sendCommand(`${flashes}, ${periodMS}`);
    };

}


main();