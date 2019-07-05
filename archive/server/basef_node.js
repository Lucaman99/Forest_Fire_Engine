
var express = require('express')
var express2 = require('express')
var app = express()
var app2 = express2()
var url = require('url')
var server = require('http').createServer(app)
var io = require('socket.io')(server)
var mysql = require('mysql')

app.get('/', function (req, res) {
	res.sendfile('b.html')
})

server.listen(3035, function () {
	console.log('Listening')
})

var con = mysql.createConnection({host: 'localhost', user: 'root', password: 'a', database: "basef"})

con.connect(function (err){
	if (err) throw err;
})

var arr = []

function one() {

	var sql = "SELECT * FROM basef2"
   con.query(sql, function(err, data){
   	if (err) throw err;

   	arr.push(decodeURI(data[data.length - 1].input))

	io.emit('event67', decodeURI(data[data.length - 1].input))


   	console.log(decodeURI(data[data.length - 1].input))

   	var base = data.length

   	function send() {
	var sql = "SELECT * FROM basef2"
   con.query(sql, function(err, data){
   	if (err) throw err;
   	if (base !== data.length) {
   		one()
   	}
   	else {
   		setTimeout(send, 100)
   	}
   })
