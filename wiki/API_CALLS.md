###Create Users

**url** clikur.xyz/api/v1/users/new <br>
**method** POST <br>
**Example Posting with cURL** <br>
curl -H "Content-Type: application/json" -X POST -d '{"NAME":"John Doe","ID":"28240567","EMAIL":"john@u.rochester.edu","PASS":"password123","PROF":"False"}' clikur.xyz/api/v1/users/new
<br>
**Output** <br>
__if success__ <br>
{<br>
  "result":"success"<br>
}<br>
__if no success_ <br>
{<br>
  "result":"no success" <br>
}<br>

###Get Users

**url** clikur.xyz/api/v1/users/<email> <br>
**method** GET <br>
**Output** <br>
__if success__ <br>
{<br>
  "email":  "john@u.rochester.edu",<br>
  "isProfessor":  "False",<br>
  "password": "password123",<br>
  "studentid": "28240567",<br>
  "userName": "John Doe"<br>
}<br>

###Create Classes

**url** clikur.xyz/api/v1/classes/new <br>
**method** POST <br>
**Example Posting with cURL** <br>
curl -H "Content-Type: application/json" -X POST -d "{'TITLE':'CSC 210','SEMESTER':'1601'}" clikur.xyz/api/v1/classes/new

###Get Classes

**url** clikur.xyz/api/v1/classes <br>
**method** GET <br>
**Output** <br>
_type_ = json <br>
[{"title": "Human Computer Interaction", "start_time": "3:25", "semester": 1501, "session": "MW", "callsign": "csc212", "end_time": "4:40"}, {"title": "Web Programming", "start_time": "4:50", "semester": 1501, "session": "TR", "callsign": "csc210", "end_time": "6:05"}]
