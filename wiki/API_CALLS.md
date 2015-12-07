###Create Users

**url** clikur.xyz/api/v1/users/new <br>
**method** POST <br>
**Input with cURL** <br>
```
curl -H "Content-Type: application/json" -X POST -d '{"NAME":"John Doe","ID":"28240567","EMAIL":"john@u.rochester.edu","PASS":"password123","PROF":"False"}' clikur.xyz/api/v1/users/new
```
<br>
**Output** <br>
_if success_ <br>
_type_ = **json** <br>
```
{
  "result":"success"
}
```
_if no success_ <br>
```
{
  "result":"no success"
}
```
<br>

###Get Users

**url** clikur.xyz/api/v1/users/<email> <br>
**method** GET <br>
**Input with cURL**<br>
```
curl -H "Content-Type: application/json" -X GET -d '{"EMAIL":"amamun@u.rochester.edu"}' localhost:8000/api/v1/users/
```
**Output** <br>
_if success_ <br>
_type_ = **json**
```
{
  "email":  "amamun@u.rochester.edu",
  "isProfessor":  "False",
  "password": "password",
  "studentid": "28210917",
  "userName": "Abdullah Al Mamun"
}
```
<br>

###Find all users

**url** clikur.xyz/api/v1/find/users
**method** GET <br>
**Output**<br>
_type_ = json array
_All users_


###Login

**url** clikur.xyz/api/v1/login <br>
**method** GET/POST <br>
**Input with cURL** <br>
```
curl -H "Content-Type: application/json" -X GET -d '{"EMAIL":"amamun@u.rochester.edu","PASS":"password"}' localhost:8000/api/v1/login
```
<br>
**Output** <br>
_type_ = json <br>
```
{
  "isProfessor": "False", 
  "result": true, 
  "token": "2df30ee5-6905-4fe2-993e-39bfe7340dce"
}
```
<br>

###Logout

**url**
**method** POST <br>
**Input with cURL** <br>
```
curl -H "Content-Type: application/json" -X POST -d '{"TOKEN":"715cafee-4797-4e10-b9f0-3020937466ac"}' localhost:8000/api/v1/logout
```
<br>
**Output** <br>
_type_ = json <br> 
```
{
  "result": "logged_out"
}
```
<br>
###Create Classes

**url** clikur.xyz/api/v1/classes/new <br>
**method** POST <br>
**Input with cURL** <br>
```
curl -H "Content-Type: application/json" -X POST -d '{"TOKEN":"2df30ee5-6905-4fe2-993e-39bfe7340dce","TITLE":"Human Computer Interaction","SEMESTER":"1501","CALLSIGN":"CSC212","CRN":"1234567","SESSION":"MW","start_time":"3:25","end_time":"4:40"}' localhost:8000/api/v1/classes/new
```
<br>
**Output**<br>
_type_ = json
success or no success <br>

###Get Classes

**url** clikur.xyz/api/v1/classes <br>
**method** GET <br>
**Input with cURL** <br>
```
curl -H "Content-Type: application/json" -X GET -d '{"TOKEN":"2df30ee5-6905-4fe2-993e-39bfe7340dce"}' localhost:8000/api/v1/classes/
``` 
<br>
**Output** <br>
_type_ = json array <br>

```
[{"title": "Human Computer Interaction", "start_time": "3:25", "semester": 1501, "session": "MW", "callsign": "CSC212", "end_time": "4:40", "crn":1234567}, {"title": "Web Programming", "start_time": "4:50", "semester": 1501, "session": "TR", "callsign": "CSC210", "end_time": "6:05", "crn":1234568}]
```
<br>

###Post Question
__Currently updating__
