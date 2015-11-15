###Create Users

**url** clikur.xyz/api/v1/users/new <br>
**method** POST <br>
**Example Posting with cURL** <br>
curl -H "Content-Type: application/json" -X POST -d "{'NAME':'John Doe','ID':'28240567','EMAIL':'john@u.rochester.edu','PASS':'password123'}" clikur.xyz/api/v1/users/new

###Get Users

**url** clikur.xyz/api/v1/users <br>
**method** GET <br>

###Create Classes

**url** clikur.xyz/api/v1/classes/new <br>
**method** POST <br>
**Example Posting with cURL* <br>
curl -H "Content-Type: application/json" -X POST -d "{'TITLE':'CSC 210','SEMESTER':'1601'}" clikur.xyz/api/v1/classes/new

###Get Classes

**url** clikur.xyz/api/v1/classes <br>
**method** GET <br>
