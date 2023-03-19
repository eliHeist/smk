const notificationArea = document.querySelector('ul[aria-labelledby="notification-area"]')
const notify_url = 'http://127.0.0.1:8000' + document.getElementById('notification-area').dataset.url;


var dangerAlertCount = false
var warningAlertCount = false

async function apiFetchItems() {
    const response = await fetch(notify_url)
    const data = await response.json()
    UI.createElement(data)
}

setTimeout(apiFetchItems, 1000)

document.getElementById('notification-area').addEventListener('click', (e) => {
    console.log('clicked');
    notificationArea.classList.toggle('d-none')
})


var sound = new Howl({
    src: ['static/assets/bell.wav']
});
function ring() {
    sound.play();
}

setTimeout(() => {
    alerts = document.querySelectorAll('.alert')
    var no = 1
    alerts.forEach(alert => {
        setTimeout(() => {
            ring()
            alert.classList.remove('hide')
        }, no*400)
        no++
    });
}, 2 * 1000);
