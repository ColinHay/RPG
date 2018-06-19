# RPG
Reddit Post Getter

Used to search subreddits and find relevant posts based on keywords.
The RPG.py file can be edited to search specific subreddits and keywords based upon two lists titled accordingly.
The script is also capable of pushing the posts to Slack.

##

<table>
  <thead>
    <tr>
      <th>Global</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td><a href="#Controller">Controller</a></td>
    <td><p>The Controller is used to interact with underlying classes and should only be initialized once in the express app.</p>
</td>
    </tr>
<tr>
    <td><a href="#Queue">Queue</a></td>
    <td><p>Queues are used to store <a href="#Payload+data">Payload data members</a>.</p>
</td>
    </tr>
<tr>
    <td><a href="#Payload">Payload</a></td>
    <td><p>Payloads are used to store data regarding individual messages.</p>
</td>
    </tr>
<tr>
    <td><a href="#Sources">Sources</a></td>
    <td><p>Sources gets data from APIs using request-promise and creates <a href="#Payload">Payload</a> instances which are added to
<a href="#Queue">Queue</a> instances. The <a href="#Controller">Controller</a> is used to interact with methods inside of Sources.</p>
</td>
    </tr>
</tbody>
</table>

##

<table>
  <thead>
    <tr>
      <th>Global</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td><a href="#request">request</a> : <code>function</code></td>
    <td><p>A variable in the global namespace called request.</p>
</td>
    </tr>
<tr>
    <td><a href="#id">id</a> : <code>number</code></td>
    <td><p>A variable in the global namespace called id. This variable is incremented by <a href="#Payload.getNextId">Payload.getNextId()</a>.</p>
</td>
    </tr>
<tr>
    <td><a href="#observatories">observatories</a> : <code>object</code></td>
    <td><p>Used by <a href="#Sources">Sources</a> when getting data from APIs.</p>
</td>
    </tr>
<tr>
    <td><a href="#weatherTypes">weatherTypes</a> : <code>object</code></td>
    <td><p>Used by <a href="#Sources">Sources</a> when getting data from APIs.</p>
</td>
    </tr>
</tbody>
</table>

<a name="Controller"></a>

## Controller
The Controller is used to interact with underlying classes and should only be initialized once in the express app.

**Kind**: global class

* [Controller](#Controller)
    * [new Controller(app)](#new_Controller_new)
    * [.sources](#Controller+sources) : [<code>Sources</code>](#Sources)
    * [.clear(interval)](#Controller+clear)
    * [.getData(interval)](#Controller+getData)


* * *

<a name="new_Controller_new"></a>

### new Controller(app)
Creates a controller.

<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>app</td><td><code>object</code></td><td><p>The express app instance.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Controller+sources"></a>

### controller.sources : [<code>Sources</code>](#Sources)
An instance of [Sources](#Sources) used to access functionality.

**Kind**: instance property of [<code>Controller</code>](#Controller)

* * *

<a name="Controller+clear"></a>

### controller.clear(interval)
Clear expired data from the [Queue](#Queue).

**Kind**: instance method of [<code>Controller</code>](#Controller)
<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>interval</td><td><code>number</code></td><td><p>Time in milliseconds between clears.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Controller+getData"></a>

### controller.getData(interval)
Uses [Sources](#Sources) to get and send data.

**Kind**: instance method of [<code>Controller</code>](#Controller)
<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>interval</td><td><code>number</code></td><td><p>Time in milliseconds between gets.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Queue"></a>

## Queue
Queues are used to store [Payload data members](#Payload+data).

**Kind**: global class

* [Queue](#Queue)
    * [new Queue(app)](#new_Queue_new)
    * [.app](#Queue+app) : <code>Object</code>
    * [.data](#Queue+data) : <code>Object</code>
    * [.add(payload)](#Queue+add)
    * [.remove(id)](#Queue+remove)
    * [.clear()](#Queue+clear)
    * [.send(id)](#Queue+send)


* * *

<a name="new_Queue_new"></a>

### new Queue(app)
Creates a Queue with a [data member](#Queue+data) and [app member](#Queue+app).

<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>app</td><td><code>object</code></td><td><p>The express app instance.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Queue+app"></a>

### queue.app : <code>Object</code>
The express app instance.

**Kind**: instance property of [<code>Queue</code>](#Queue)

* * *

<a name="Queue+data"></a>

### queue.data : <code>Object</code>
The Queue data.

**Kind**: instance property of [<code>Queue</code>](#Queue)

* * *

<a name="Queue+add"></a>

### queue.add(payload)
Adds data from a [Payload data member](#Payload+data) to the [Queue data member](#Queue+data).

**Kind**: instance method of [<code>Queue</code>](#Queue)
<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>payload</td><td><code>object</code></td><td><p><a href="#Payload">Payload</a></p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Queue+remove"></a>

### queue.remove(id)
Removes data with matching id property from the [Queue data member](#Queue+data).

**Kind**: instance method of [<code>Queue</code>](#Queue)
<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>id</td><td><code>string</code></td><td><p>The id of the data to remove.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Queue+clear"></a>

### queue.clear()
is greater than the [expirationTime](#Payload+data) property of the data.t time](#Payload.getTimestamp)

**Kind**: instance method of [<code>Queue</code>](#Queue)

* * *

<a name="Queue+send"></a>

### queue.send(id)
Sends property from the [Queue data member](#Queue+data) with matching id using SSE.

**Kind**: instance method of [<code>Queue</code>](#Queue)
<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>id</td><td><code>string</code></td><td><p>The id of the data to send.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Payload"></a>

## Payload
Payloads are used to store data regarding individual messages.

**Kind**: global class

* [Payload](#Payload)
    * [new Payload()](#new_Payload_new)
    * _instance_
        * [.data](#Payload+data) : <code>object</code>
        * [.add(name, value)](#Payload+add) ⇒ <code>string</code>
    * _static_
        * [.getNextId()](#Payload.getNextId) ⇒ <code>number</code>
        * [.getTimestamp()](#Payload.getTimestamp) ⇒ <code>number</code>


* * *

<a name="new_Payload_new"></a>

### new Payload()
Creates a Payload with a [data member](#Payload+data).


* * *

<a name="Payload+data"></a>

### payload.data : <code>object</code>
The Payload data.

**Kind**: instance property of [<code>Payload</code>](#Payload)
**Properties**

<table>
  <thead>
    <tr>
      <th>Name</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>id</td><td><code>number</code></td><td><p><a href="#Payload.getNextId">getNextId()</a></p>
</td>
    </tr><tr>
    <td>receivedTime</td><td><code>number</code></td><td><p><a href="#Payload.getTimestamp">getTimestamp()</a></p>
</td>
    </tr><tr>
    <td>expirationTime</td><td><code>number</code></td><td><p><a href="#Payload.getTimestamp">getTimestamp()</a></p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Payload+add"></a>

### payload.add(name, value) ⇒ <code>string</code>
Adds property to [data](#Payload+data).

**Kind**: instance method of [<code>Payload</code>](#Payload)
**Returns**: <code>string</code> - Debug information.
<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>name</td><td><code>string</code></td><td><p>The name of the property to add.</p>
</td>
    </tr><tr>
    <td>value</td><td><code>string</code></td><td><p>The value of the property to add.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Payload.getNextId"></a>

### Payload.getNextId() ⇒ <code>number</code>
Gets next [id](#id).

**Kind**: static method of [<code>Payload</code>](#Payload)
**Returns**: <code>number</code> - The unique id.

* * *

<a name="Payload.getTimestamp"></a>

### Payload.getTimestamp() ⇒ <code>number</code>
Get timestamp.

**Kind**: static method of [<code>Payload</code>](#Payload)
**Returns**: <code>number</code> - The Unix timestamp in seconds.

* * *

<a name="Sources"></a>

## Sources
[Queue](#Queue) instances. The [Controller](#Controller) is used to interact with methods inside of Sources.to

**Kind**: global class

* [Sources](#Sources)
    * [new Sources(app)](#new_Sources_new)
    * [.obsWeather](#Sources+obsWeather) : [<code>Queue</code>](#Queue)
    * [.getObsWeather()](#Sources+getObsWeather)


* * *

<a name="new_Sources_new"></a>

### new Sources(app)
Creates a Sources with instances of [Queue](#Queue).

<table>
  <thead>
    <tr>
      <th>Param</th><th>Type</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>app</td><td><code>object</code></td><td><p>The express app instance.</p>
</td>
    </tr>  </tbody>
</table>


* * *

<a name="Sources+obsWeather"></a>

### sources.obsWeather : [<code>Queue</code>](#Queue)
Observatory Weather

**Kind**: instance property of [<code>Sources</code>](#Sources)

* * *

<a name="Sources+getObsWeather"></a>

### sources.getObsWeather()
added to the [data member of the Queue instance](#Queue+data).of the Payload instance](#Payload+data) is

**Kind**: instance method of [<code>Sources</code>](#Sources)

* * *

<a name="request"></a>

## request : <code>function</code>
A variable in the global namespace called request.

**Kind**: global variable

* * *

<a name="id"></a>

## id : <code>number</code>
A variable in the global namespace called id. This variable is incremented by [Payload.getNextId()](#Payload.getNextId).

**Kind**: global variable

* * *

<a name="observatories"></a>

## observatories : <code>object</code>
Used by [Sources](#Sources) when getting data from APIs.

**Kind**: global variable
**Properties**

<table>
  <thead>
    <tr>
      <th>Name</th><th>Type</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>teide</td><td><code>string</code></td>
    </tr><tr>
    <td>chile</td><td><code>string</code></td>
    </tr>  </tbody>
</table>


* * *

<a name="weatherTypes"></a>

## weatherTypes : <code>object</code>
Used by [Sources](#Sources) when getting data from APIs.

**Kind**: global variable
**Properties**

<table>
  <thead>
    <tr>
      <th>Name</th><th>Type</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>temperature</td><td><code>string</code></td>
    </tr><tr>
    <td>dewpoint</td><td><code>string</code></td>
    </tr><tr>
    <td>humidity</td><td><code>string</code></td>
    </tr><tr>
    <td>windspeed</td><td><code>string</code></td>
    </tr><tr>
    <td>windgust</td><td><code>string</code></td>
    </tr>  </tbody>
</table>


* * *

