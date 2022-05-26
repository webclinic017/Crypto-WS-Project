
var chart = LightweightCharts.createChart(document.getElementById("chart"), {
	width: 600,
  height: 300,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: 'rgba(0, 255, 0, 1)',
  downColor: 'rgba(255, 0, 0, 1)',
  borderDownColor: 'rgba(255, 0, 0, 1)',
  borderUpColor: 'rgba(0, 255, 0, 1)',
  wickDownColor: 'rgba(255, 0, 0, 1)',
  wickUpColor: 'rgba(0, 255, 0, 1)',
});

// WARNING: current fetch url only works in dev mode
fetch('http://127.0.0.1:5000/history')
	.then((r) => r.json())
	.then((response) => {
		//console.log(response);
		candleSeries.setData(response);
	})

var ws = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_5m");
ws.onmessage = (event) => {
    let stockObj = JSON.parse(event.data);
    let candlestick = stockObj.k;
	console.log("open (chart.js) " + candlestick.o)
	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}