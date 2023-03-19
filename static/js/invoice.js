const button = document.querySelectorAll('.add-order')
const itemList = document.getElementById('items')
const orderList = document.getElementById('current-items-list')
var customerId = document.querySelector('#customer-select').value


//#region models
class Order {
    constructor(itemId, quantity) {
        this.itemId = itemId;
        this.quantity = quantity;
    }
}
class Item {
    constructor(id, name, price, stock) {
        this.id = id
        this.name = name
        this.price = price
        this.stock = stock
    }
}
//#endregion

//#region listen events
const orderItem = (e) => {
    const btn = e.target
    if (btn.classList.contains('add-order')) {
        // get data
        const action = btn.dataset.action
        const id = btn.dataset.item
        const name = btn.dataset.name
        const price = btn.dataset.price
        const stock = btn.dataset.stock
        const item = new Item(id * 1, name, price * 1, stock * 1)
        if (action === 'add') {
            UI.addToSale(item)
        }
    }
}

const saleManager = (e) => {
    const element = e.target
    if (element.classList.contains('delete-order')) {
        UI.deleteOrder(element.parentElement.parentElement)
    } else if (element.type === 'number') {
        element.addEventListener('change', () => {
            if (element.value * 1 <= 0) {
                UI.deleteOrder(element.parentElement.parentElement)
            } else if (element.value * 1 === element.dataset.stock * 1) {
                element.disabled = true
            } else {
                const id = element.dataset.id
                const price = element.dataset.price
                document.getElementById('data-cost' + id).innerText = price * element.value
                // update objarray
                const order = new Order(id * 1, element.value * 1)
                OBJ.updateOrder(order)
                UI.updateTotalCost()
            }
        })
    }
}

itemList.addEventListener('click', orderItem)
orderList.addEventListener('click', saleManager)
//#endregion

//#region UI actions
document.querySelector('#customer-select').addEventListener('change', (e) => {
    customerId = e.target.value
    discount = document.querySelector(`option[value="${customerId}"]`).dataset.discount*1
    UI.updateTotalCost()
})
//#endregion

//#region orders json object
var orderObjects = []

class OBJ {
    static addOrder(order) {
        var obj = {
            'item': order.itemId,
            'quantity': order.quantity
        }
        orderObjects.push(obj)
    }
    static updateOrder(order) {
        orderObjects.forEach(object => {
            if (object.item == order.itemId) {
                object.quantity = order.quantity
            }
        });
    }
    static removeOrder(orderid) {
        
        for (var i = 0; i < orderObjects.length; i++) {
            if (orderObjects[i].item === orderid) {
                orderObjects.splice(i, 1);
            }
        }
    }
}
//#endregion

const checkoutBtn = document.getElementById('checkout')
const tokenDiv = document.querySelector('input[name="csrfmiddlewaretoken"]')
const apiLink = checkoutBtn.dataset.apilink
var csrftoken = tokenDiv.value


checkoutBtn.addEventListener('click', (e) =>{
    e.preventDefault()
    if (orderObjects.length > 0) {
        
        orderObjects.forEach(obj => {
            obj.customer = customerId
        });
        API.postOrders(orderObjects)
    }
})

//#region API's
class API{
    static postOrders(orders){
        fetch(apiLink, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
                'customer':0,
            },
            body:JSON.stringify(orders)
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            if (data === 'success') {
                document.location.reload()
            }
        })
    }
}
//#endregion

