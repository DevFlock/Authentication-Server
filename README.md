# Authentication-Server
Bad authentication server, need to add more features since right now just an api wrapper for a database. Meant to be run with docker compose with your own website/whatever else you want to build.

Since I am no where near a security expert, this should not be used in any serious situations. Only way it proves that the user is validated is by returning an error, and if not used correctly could be spoofed. And it requires https since passwords are sent in plain text and are only encrypted when being stored in the database.

