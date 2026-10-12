async function sendFlash(flashes, periodMS){
    var response = await fetch(`/api/${flashes}/${periodMS}`);
    var replyText = await response.text();
    
    console.log(replyText)
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText
}

async function sendLEDState(LEDState){
    var response = await fetch(`/api/${LEDState}`);
    var replyText = await response.text();
    
    console.log(replyText)
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText
}

function main() {
    console.log("Hello JavaScript!");
    document.querySelector('#on').onclick = () => {
        console.log("You pressed the ON button!");
        sendLEDState("LED ON")
    };
    document.querySelector('#off').onclick = () => {
        console.log("You pressed the OFF button!");
        sendLEDState("LED OFF")
    };
    
    document.querySelector('#flash').onclick = () => {
        let flashes = document.querySelector("#flashes").value;
        let periodMS = document.querySelector("#periodMS").value;
        console.log("FLASH!");
        sendFlash(flashes, periodMS);
    };

}


main();