//Globals
let PLAYER_ID = null
let GAME_STATE = null
let PLAYERS = []
let OBJECTS = []

// Server events
let socket = io()
socket.on("connect", () => {
    socket.emit("event1", "hello")
})

socket.on("assign_id", (id) => {
    PLAYER_ID = id["data"]
})

socket.on("update", (data) => {
    objects = data["objects"]
    objects.forEach((object, i) => {
        OBJECTS.push(object)
    })
})
///////////////////////////////////////////

const canvas = document.getElementById("c-main")
const ctx = canvas.getContext("2d")

canvas.width = window.innerWidth
canvas.height = window.innerHeight

canvas.addEventListener("click", (event) => {
    mouseX = event.clientX
    mouseY = event.clientY
    socket.emit("click", {data: {player_id: PLAYER_ID, x: mouseX, y: mouseY}})
})

function draw() {
    ctx.fillStyle = "black"
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = "blue"
    OBJECTS.forEach((object, i) => {
        ctx.fillRect(object.x, object.y, 50, 50)
    })
}

function loop() {
    window.requestAnimationFrame(loop)
    draw()
}

loop()