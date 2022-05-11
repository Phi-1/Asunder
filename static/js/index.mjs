import ShipSelection from "./ShipSelection.mjs"

const socket = io()

socket.on("get_ship_selection", (data) => {
    ShipSelection.init(data["ships"])
})

function main() {
    socket.emit("get_ship_selection")
}

main()