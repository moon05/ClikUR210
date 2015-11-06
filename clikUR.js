//  Steps:
// 	1) npm install express
//  2) npm install body-parser
//  3) [RUN] node server.js

var exp = require('express');
var app = express();

var parser = require('body-parser');
app.use(parser.json());
app.use(parser.urlencoded({ extended: true }));

//static-files is where all of the other files (HTML, JPG etc.) are stored
app.use(exp.static('static_files'));

// CREATE a new user
app.post('/users', function (req, res) {
  var postBody = req.body;
  var ID = postBody.id;

  // must have a Student ID #!
  if (!ID) {
    res.send('ERROR');
    return;
  }

  // check if user's name is already in database; if so, send an error
  for (var i = 0; i < Database.length; i++) {
    var e = Database[i];
    if (e.name == ID) {
      res.send('ERROR');
      return;
    }
  }

  Database.push(postBody);

  res.send('OK');
