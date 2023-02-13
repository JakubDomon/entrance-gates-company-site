// Moving Gradient
var granimInstance = new Granim({
    element: '#granim-canvas',
    name: 'granim',
    opacity: [1, 1],
    states : {
        "default-state": {
            gradients: [
                ['#ededed', '#ededed'],
                ['#d7d7d7', '#dfdfdf']
            ],
            transitionSpeed: 3000
        }
    }
});