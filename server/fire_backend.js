var express = require('express')
var app = express()
var express2 = require('express')
var app2 = express()
var http = require('http').createServer(app)
var http2 = require('http').createServer(app2)
var io = require('socket.io')(http)
var io2 = require('socket.io')(http2)
var mysql = require('mysql')
var fs = require('fs')
var url = require('url')

app.get("/", function (req, res) {
  res.sendfile("fire_alert.html")
})

app2.get("/", function (req, res) {
  res.sendfile("testing_alert.html")
})

io2.on("connection", function (socket){
  console.log("A user has connected")

  socket.on('fire_event', function (data){
    console.log("Received")
    io.emit('event_flame', data)
  })

})

var server = http.listen(8081, function () {
  console.log("Listening...")
})

var server2 = http2.listen(8082, function () {
  console.log("Listening...")
})
