var ws = new WebSocket('wss://stream.binance.com:9443/ws/etheur@trade');
var dataDiv = document.getElementById('data');
ws.onmessage = (event) => {
    let stockObj = JSON.parse(event.data);
    dataDiv.append(stockObj.p);
}