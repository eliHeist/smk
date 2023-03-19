var discount


class UI {
    //#region notifications
    static createElement = (items) => {
        items.forEach(item => {
            if (item.stock === 0) {
                UI.createAlert(item, 'danger', 'Out of stock')
                
            }
        });
        items.forEach(item => {
            if (item.stock < item.minimum_stock && item.stock !== 0) {
                UI.createAlert(item, 'warning', 'Low stock')
            }
        });
    }

    static createAlert(item, className, message) {
        function createHeader(class_name, header) {
            const row = document.createElement('li')
            row.innerHTML = `<h3 class="dropdown-header h6 text-${class_name}">${header}</h3>`
            notificationArea.appendChild(row)
        }

        function addAlert(item, class_name) {
            const row = document.createElement('li')
            row.classList.add('alert', `alert-${class_name}`, 'hide')
            row.innerHTML = `${item.id}: ${item.name}, ${item.stock}`
            notificationArea.appendChild(row)
        }
        if (className === 'danger' && !dangerAlertCount) {
            createHeader('danger', message)
            dangerAlertCount = true
        }
        if (className === 'warning' && !warningAlertCount) {
            createHeader('warning', message)
            warningAlertCount = true
        }
        addAlert(item, className)
    }
    //#endregion

    //#region invoices
    static addToSale(item) {
        var list = document.getElementById('current-items-list')
        if (list.children.length >= 1) {
            // loop through xisting rows and return add or update actions
            function loop(item, list) {
                for (let index = 0; index < list.children.length; index++) {
                    const child = list.children[index];
                    if (child.dataset.item * 1 === item.id) {
                        return 'update'
                    }
                }
                return 'add'
            }
            var action = loop(item, list)
            // create with returned action
            UI.createOrderUi(item, action)
        } else {
            UI.createOrderUi(item, 'add')
        }

    }
    static createOrderUi(item, action) {
        var list = document.getElementById('current-items-list')
        if (action === 'add') {
            const row = document.createElement('li')
            row.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center')
            row.setAttribute('data-item', item.id)
            row.innerHTML = `
            <div class="d-flex align-items-center">
                <input readonly data-stock="${item.stock}" data-price="${item.price}" data-id="${item.id}" type="number" id="data-count${item.id}" name="order1" value="${1}" class="n-o-items" style="width: 3em; border: 0;">
                <i id="data-item" class=" text-primary ">${item.name}</i>
            </div>
            <div class="d-flex align-items-center">
            <i class="fas fa-tag text-muted fs-6">Shs. </i>
            <i class="fas ms-2 text-muted fs-6 order-price" id="data-cost${item.id}">${item.price}</i>
            <i class='fas fa-times fs-5 ms-2 text-danger delete-order' role='button'></i>
            </div>
            `
            // add created item
            list.appendChild(row);
            // add to objarray
            const order = new Order(item.id * 1, 1)
            OBJ.addOrder(order)
            // update total
            UI.updateTotalCost()
        } else if (action === 'update') {
            for (let index = 0; index < list.children.length; index++) {
                const child = list.children[index];
                if (child.dataset.item * 1 === item.id) {
                    // update if its value is not greater than stock
                    if (document.getElementById("data-count" + item.id).value * 1 < item.stock) {
                        document.getElementById("data-count" + item.id).value++
                        var newPrice = item.price * document.getElementById("data-count" + item.id).value
                        document.getElementById("data-cost" + item.id).innerText = newPrice
                        // update objarray
                        const order = new Order(item.id * 1, document.getElementById("data-count" + item.id).value * 1)
                        OBJ.updateOrder(order)
                        // update total
                        UI.updateTotalCost()
                    }
                }
            }
        }
    }
    static updateTotalCost() {
        var total = 0
        const list = document.querySelectorAll('.order-price')
        const btn = document.getElementById('checkout')
        list.forEach(cost => {
            total += cost.innerText * 1
        });
        if (discount) {
            var _discount = total * discount / 100
            total -= _discount
            console.log(total + ' total');
        }
        btn.value = formatter.format(total)
    }
    static deleteOrder(element) {
        if (element.children[1].children[2].classList.contains('delete-order')) {
            element.remove();
        }
        // delete from objarray
        const id = element.dataset.item * 1
        OBJ.removeOrder(id)
        // update total
        UI.updateTotalCost()
    }
    //#endregion
}