###Create Users

**url** clikur.xyz/api/v1/users/new
**method** POST
**Example Posting with cURL**
curl -H "Content-Type: application/json" -X POST -d "{'NAME':'John Doe','ID':'28240567','EMAIL':'john@u.rochester.edu','PASS':'password123'}" clikur.xyz/api/v1/users/new

###Get Users

**url** clikur.xyz/api/v1/users
**method** GET

###Create Classes

**url** clikur.xyz/api/v1/classes/new
**method** POST
**Example Posting with cURL*
curl -H "Content-Type: application/json" -X POST -d "{'TITLE':'CSC 210','SEMESTER':'1601'}" clikur.xyz/api/v1/classes/new

###Get Classes

**url** clikur.xyz/api/v1/classes
**method** GET
