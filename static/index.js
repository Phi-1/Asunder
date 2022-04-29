let socket = io()
socket.on("connect", () => {
    socket.emit("event1", "hello")
})
///////////////////////////////////////////

const canvas = document.getElementById("c-main")
const ctx = canvas.getContext("2d")

canvas.width = window.innerWidth
canvas.height = window.innerHeight

function draw() {
    ctx.fillStyle = "black"
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = "yellow"
    ctx.fillRect(canvas.width - 1, canvas.height - 1, 1, 1)
}

function loop() {
    window.requestAnimationFrame(loop)
    draw()
}

loop()