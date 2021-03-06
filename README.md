# Quoted

The restful quote api.

Quoted is basically a set of tools to create a REST API for quotes. It tries to be as flexible as possible by using Mongo dynamic documents to store the data therefore it is possible to add as many data points as you see fit such as author, description, themes, etc. Although with great power comes great responsibility to maintain consistency and intuitiveness.

## The REST API

The backend API implements all your usual REST methods (`GET`, `POST`, `PUT` and delete) for manipulating quote documents. For the following examples I'll use `curl` but use whatever. I'll also use `localhost:5000` as the uri as that is the default but replace it to fit your needs. The following not only work for the `/quotes` endpoint but also for `/characters` and `/themes`.

`/characters` and `/themes` are also automatically updated when you create a quote with `character` and/or `themes` (which is a list of strings), property.

(I'm sorry in advance for the terrible heading names.)

### GETting quotes

To get a list of all the quotes in the database:

`$ curl -i http://localhost:5000/api/v1.0/quotes`

Here we'll see all the quotes and all the data points for those quotes.

```
{
  "quotes": []
}
```

Which is currently nothing so we should change that!

### POSTing new quotes into the database

To create a new quote:

`$ curl -i -H "Content-Type: application/json" -X POST -d '{"quote":"Hello World", "significance":"The first text sent over the Internet"}' http://localhost:5000/api/v1.0/quotes`

The only required property is `quote` but you can add as many arbitrary properties to a quote as you see fit. Here I added a `significance` property to the quote.

The newly created quote entry will be returned.

```
{
  "quote": {
    "_id": {
      "$oid": "5d97d97b6d233119916e3e84"
    },
    "quote": "Hello World",
    "uri": "http://localhost:5000/api/v1.0/quotes/5d97d97b6d233119916e3e84",
    "significance": "The first text sent over the Internet"
  }
}
```

Keep note of the `$oid` value. This is Mongo's internal id value which is used to index a quote. For convenience, the `uri` value is generated which can be used to retrieve that specific quote via a `GET` request and apply operations to it.

### PUTting updated values into a quote

To modify an existing quote:

`$ curl -i -H "Content-Type: application/json" -X PUT -d '{"significance":"A Hello world program is a computer program that outputs Hello World (or some variant) on a display device."}' http://localhost:5000/api/v1.0/quotes/5d97d97b6d233119916e3e84`

Here we are modifying the `significance` property for our quote (which has the id of `5d97d97b6d233119916e3e84`) but the same syntax can also be used to create new properties. Deleting properties can be done through setting them to and empty string ("").

This will return our modified quote:

```
{
  "quote": {
    "_id": {
      "$oid": "5d97d97b6d233119916e3e84"
    },
    "quote": "Hello World",
    "uri": "http://localhost:5000/api/v1.0/quotes/5d97d97b6d233119916e3e84",
    "significance": "A Hello world program is a computer program that outputs Hello World (or some variant) on a display device."
  }
}
```

### DELETEing a quote

To delete a quote:

`curl -i -X DELETE http://localhost:5000/api/v1.0/quotes/5d97d97b6d233119916e3e84`

Which will return nothing as there's nothing.

## Licence

Quoted is distributed under the MIT Licence.
