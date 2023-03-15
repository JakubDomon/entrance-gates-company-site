// Event to reload page after form is successful
document.body.addEventListener('successRefresh', (event) =>{
    setTimeout(() => {
        document.location.reload()
    }, 2000)
})