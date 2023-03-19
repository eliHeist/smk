var formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'UGX',

    // These options are needed to round to whole numbers 
    //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
    //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
});
var formatter2 = new Intl.NumberFormat('en-US', {
    // style: 'currency',
    // currency: 'Shs',

    // These options are needed to round to whole numbers 
    //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
    //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
});


// currency
const money_divs = document.querySelectorAll('.currency_format')

money_divs.forEach(div => {
    div.innerText = formatter2.format(div.innerText)
});