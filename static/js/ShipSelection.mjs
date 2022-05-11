import Classnames from "./Classnames.mjs"

class Ship {
    constructor(name, image_path) {
        this.name = name
        this.image_path = image_path
    }
}

export default class ShipSelection {

    static e_title = document.querySelector(`.${Classnames.spaceship_selection.title}`)
    static e_arrow_left = document.querySelector(`.${Classnames.spaceship_selection.arrow_left}`)
    static e_arrow_right = document.querySelector(`.${Classnames.spaceship_selection.arrow_right}`)
    static e_image = document.querySelector(`.${Classnames.spaceship_selection.image}`)
    static ships = []
    static index = 0
    
    static init(ships) {
        for (let i in ships) {
            ShipSelection.ships.push(new Ship(ships[i]["name"], ships[i]["image"]))
        }
        ShipSelection.e_arrow_left.addEventListener("click", ShipSelection.left_arrow_event)
        ShipSelection.e_arrow_right.addEventListener("click", ShipSelection.right_arrow_event)
        ShipSelection.render()
    }

    static get_selected_ship() {
        return ShipSelection.ships[ShipSelection.index].name
    }

    static render() {
        const ship = ShipSelection.ships[ShipSelection.index]
        ShipSelection.e_title.innerHTML = ship.name
        ShipSelection.e_image.style["background-image"] = `url(static/img/${ship.image_path})`
    }

    static left_arrow_event(event) {
        if (ShipSelection.index == 0) { ShipSelection.index = ShipSelection.ships.length - 1 }
        else { ShipSelection.index-- }
        ShipSelection.render()
    }

    static right_arrow_event(event) {
        if (ShipSelection.index == ShipSelection.ships.length - 1) { ShipSelection.index = 0 }
        else { ShipSelection.index++ }      
        ShipSelection.render()
    }

}