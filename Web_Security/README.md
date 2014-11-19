# Web Security

* Steps of web exploitation:
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
```
Once we have identified and downloaded *.swf files, we must analyze the code, the functions (as *loadMovie*) variables in order to identify those that call and allow other types of vulnerabilities such as cross site scripting. Below shows some vulnerable functions:
```
_root.videourl = _root.videoload + '.swf';
video.loadMovie(_root.videourl);
getURL - payload. javascript:alert('css') getURL (clickTag, '_self')
	load* (in this case: loadMovie) - payload: as
function.getURL,javascript:alert('css')
	TextField.html - payload: <img src='javascript:alert("css")//.swf'>
```

We could use tools such as **Deblaze** and **SWFIntruder**. We should also
analyze the parameter AllowScriptAccess, Flash Parameter Pollution or sensitive APIs:
```
loadVariables, loadVariblesNum, MovieClip.loadVariables, loadVars.load, loadVars.sendAndLoad
XML.load, XML.sendAndLoad
URLLoader.load, URLStream.load
LocalConnection
ExternalInterface.addCallback
SharedObject.getLocal, SharedObject.getRemote
```

		* authentication system: the first thing is to determine if the website stored the credentials in the browser. This could be exploited with attacks on defaults accounts and dictionary attacks. The default accoints are: admin, administrator, root, system, user, default, name application. We can use **hydra** for this:
```
$ hydra -L users.txt -P pass.txt <WEBSTE> http-head/private
```


* [My list of common web vulnerabilities.](http://bt3gl.github.io/a-list-of-common-web-vulnerabilities.html)

## OS Command Injection

---

## SQLi

- Brute force password
- Timed SQLi
- Cookie force brute


--- 
## PHP Shells

- php primer
- xor
- exploits



-----
## User ID
- cookie auth
- user id

----

## Other Resources

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

The first line of a request is modified to include protocol version information and it's followed by zero or more name:value pairs (headers):
- User-Agent: browser version information
- Host: URL hostanme
- Accept: supported MIME documents( such as text/plain or audio/MPEG)
- Accept-Language: supported language codes
- Referer: originating page for the request

The headers are terminated with a single empty line, which may be followerd by any payload the client wishes to pass to the server (the lenght should be specified with the Content-Length header). The  payload is usually browser data, but there is no requirements.



-----
## Tools

- [Burp Suite]
- [FireBug] in Firefox

----

## CSRF

Identification and verification manual of CSRF can be done by checking in the website's forms (usually where most often find this vulnerability). 

To check this, you will need to copy an original request (GET / POST) on a form and then make a change in the parameters and re-send the same request modified. If the server does not return an error, it can be considered that it is vulnerable to
CSRF. 

To perform this task, we can use the tools **csrftester** or **burp** proxy.




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

