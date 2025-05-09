var express = require('express');
var app = express();
const fs = require('fs')

// name file read
function rsl(){
   fs.readFile('./stu/students.json', 'utf-8', (err, data) => {
      if (err){
         console.error(err);
      }
      //console.log(data);
      var data1 = JSON.parse(data)
      return data1;
   })
}
var s = rsl()

console.log(s)
//  主页输出 "Hello World"
app.get('/', function (req, res) {
   console.log("主页 GET 请求");
   res.sendFile(`${__dirname}/index.html`);
})
 
//  POST 请求
app.post('/login', function (req, res) {
   console.log("主页 POST 请求");

   res.send('Hello POST');
})
//sign in
app.post('/signin', function (req, res) {
   console.log("主页 POST 请求");
   res.send('Hello POST');
})
 
var server = app.listen(8081, function () {
 
  var host = server.address().address;
  var port = server.address().port;
 
  console.log("应用实例，访问地址为 http://%s:%s", host, port);
 
})
