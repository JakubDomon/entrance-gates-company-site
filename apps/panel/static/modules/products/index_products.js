function deleteElement(elemName){
    var ask = window.confirm('Na pewno chcesz usunąć '+elemName+'?');
    if(ask){
        window.alert('Pomyślnie usunięto '+elemName+'')
    }
    return false
}