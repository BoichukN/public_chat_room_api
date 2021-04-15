Django application - public chat room(only RESTful API).

Unauthenticated users can post messages via API in chat so others can read them.



API methods:

- GET method for getting all messages with pagination by 10 messages per request.

e.g.

/api/messages/list/0 will return first 10 messages

/api/messages/list/1 will return second 10 messages

etc

- GET method for getting single message by unique identifier

e.g.

/api/messages/single/123

- POST method for creating a new message

Body accepts email and text.
