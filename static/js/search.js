searchbar = document.querySelector('#searchbar')
searchbar.addEventListener('keyup', searchItems);


function searchItems(e) {
    var text = e.target.value.toLowerCase();
    var items = document.querySelectorAll('tr[role="item"]')
    Array.from(items).forEach((item)=>{
        var itemName = item.children[1].textContent;
        var brandName = item.children[2].textContent;
        if (itemName.toLowerCase().indexOf(text) != -1 || brandName.toLowerCase().indexOf(text) != -1) {
            if (item.classList.contains('d-none')) {
                item.classList.remove('d-none')
            }
        } else {
            if (!item.classList.contains('d-none')) {
                item.classList.add('d-none')
            }
        }
    })
}