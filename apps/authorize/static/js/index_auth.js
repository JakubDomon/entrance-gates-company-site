// Check if redirect after successful register
const action = data.action;
var redirectTime = 5; 

console.log(action);
const secondSpan = document.querySelector('#seconds');

// Countdown and redirect
if(action == 'redirect'){
    setInterval(()=>{
        if(redirectTime != 0){
            secondSpan.innerHTML = redirectTime;
            redirectTime--;
        }
    }, 1000)
    setTimeout(()=>{
        window.location.replace('/')
    }, redirectTime*1000)
}