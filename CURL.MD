# curl

HTTPリクエスト コマンド

## GET

`$ curl -sS localhost/ctf/question`

-sS は余計なプログレスバーとかは出力しないが、エラーは出力するオプション

## ファイルに出力

`$ curl -sS localhost/ctf/question -o aaa.txt`

-O でリクエスト先の名前でファイル保存

`$ curl -sS localhost/ctf/question -O
$ cat question`

## HTTP Headerを確認する

### -I Headerのみ

`$ curl -sS localhost/ctf/question -I`

### -i Header, Body 両方

`$ curl -sS localhost/ctf/question -i`

### -v リクレストHeaderも

`$ curl -sS localhost/ctf/question -v`

## POST

--dataにセットするパラメータ値が英数字以外のときは、URLエンコードが必要です。

    $ curl -sS -i localhost/ctf/question/1 -X POST --data 'flag=sasakama@matsushima'
    HTTP/1.1 302 Found
    Date: Tue, 09 Jan 2018 07:39:55 GMT
    Server: Apache-Coyote/1.1
    Location: http://10.132.83.231/ctf/question/1/good
    Content-Language: ja-JP
    Content-Length: 0
    Set-Cookie: JSESSIONID=D0DAB5A78F64098D59282AAE1954DA24; Path=/ctf/; HttpOnly
    Connection: close
    Content-Type: text/plain; charset=UTF-8


## BASIC認証(-u)

`$ curl -sS 'http://10.132.83.253:8515/api/json' -u jenkins:jenkin`

## SessionをCookieから取得して使用 (-c -b)

-c cookie.txt で、レスポンスのCookieをcookie.txtに保存し、
-b cookie.txt で、cookie.txtの中身をリクエストのCookieに含めることができます。

## HTTPステータスだけを表示

`$ curl -sS -w '%{http_code}\n' localhost/ctf/question -o /dev/null`

## URLエンコードするだけ

    $ curl -s -w '%{url_effective}\n' --data-urlencode 'じぇんきんす' -G ''
    /?%E3%81%98%E3%81%87%E3%82%93%E3%81%8D%E3%82%93%E3%81%99
    
## User-Agentを偽装する(-A ''で空にする)

    $ curl -s -w '%{http_code}\n' http://www.amazon.co.jp/dp/B00JEYPPOE/ -o /dev/null 
    503
    $ curl -s -w '%{http_code}\n' http://www.amazon.co.jp/dp/B00JEYPPOE/ -o /dev/null  -A ''
    200
    
## オプション

    $ curl --help
    Usage: curl [options...] <url>
    Options: (H) means HTTP/HTTPS only, (F) means FTP only
        --anyauth       Pick "any" authentication method (H)
     -a/--append        Append to target file when uploading (F/SFTP)
        --basic         Use HTTP Basic Authentication (H)
        --cacert <file> CA certificate to verify peer against (SSL)
        --capath <directory> CA directory to verify peer against (SSL)
     -E/--cert <cert[:passwd]> Client certificate file and password (SSL)
        --cert-type <type> Certificate file type (DER/PEM/ENG) (SSL)
        --ciphers <list> SSL ciphers to use (SSL)
        --compressed    Request compressed response (using deflate or gzip)
     -K/--config <file> Specify which config file to read
        --connect-timeout <seconds> Maximum time allowed for connection
     -C/--continue-at <offset> Resumed transfer offset
     -b/--cookie <name=string/file> Cookie string or file to read cookies from (H)
     -c/--cookie-jar <file> Write cookies to this file after operation (H)
        --create-dirs   Create necessary local directory hierarchy
        --crlf          Convert LF to CRLF in upload
        --crlfile <file> Get a CRL list in PEM format from the given file
     -d/--data <data>   HTTP POST data (H)
        --data-ascii <data>  HTTP POST ASCII data (H)
        --data-binary <data> HTTP POST binary data (H)
        --data-urlencode <name=data/name@filename> HTTP POST data url encoded (H)
        --delegation STRING GSS-API delegation permission
        --digest        Use HTTP Digest Authentication (H)
        --disable-eprt  Inhibit using EPRT or LPRT (F)
        --disable-epsv  Inhibit using EPSV (F)
     -D/--dump-header <file> Write the headers to this file
        --egd-file <file> EGD socket path for random data (SSL)
        --engine <eng>  Crypto engine to use (SSL). "--engine list" for list
     -f/--fail          Fail silently (no output at all) on HTTP errors (H)
     -F/--form <name=content> Specify HTTP multipart POST data (H)
        --form-string <name=string> Specify HTTP multipart POST data (H)
        --ftp-account <data> Account data to send when requested by server (F)
        --ftp-alternative-to-user <cmd> String to replace "USER [name]" (F)
        --ftp-create-dirs Create the remote dirs if not present (F)
        --ftp-method [multicwd/nocwd/singlecwd] Control CWD usage (F)
        --ftp-pasv      Use PASV/EPSV instead of PORT (F)
     -P/--ftp-port <address> Use PORT with address instead of PASV (F)
        --ftp-skip-pasv-ip Skip the IP address for PASV (F)
        --ftp-ssl       Try SSL/TLS for ftp transfer (F)
        --ftp-ssl-ccc   Send CCC after authenticating (F)
        --ftp-ssl-ccc-mode [active/passive] Set CCC mode (F)
        --ftp-ssl-control Require SSL/TLS for ftp login, clear for transfer (F)
        --ftp-ssl-reqd  Require SSL/TLS for ftp transfer (F)
     -G/--get           Send the -d data with a HTTP GET (H)
     -g/--globoff       Disable URL sequences and ranges using {} and []
     -H/--header <line> Custom header to pass to server (H)
     -I/--head          Show document info only
     -h/--help          This help text
        --hostpubmd5 <md5> Hex encoded MD5 string of the host public key. (SSH)
     -0/--http1.0       Use HTTP 1.0 (H)
        --ignore-content-length  Ignore the HTTP Content-Length header
     -i/--include       Include protocol headers in the output (H/F)
     -k/--insecure      Allow connections to SSL sites without certs (H)
        --interface <interface> Specify network interface/address to use
     -4/--ipv4          Resolve name to IPv4 address
     -6/--ipv6          Resolve name to IPv6 address
     -j/--junk-session-cookies Ignore session cookies read from file (H)
        --keepalive-time <seconds> Interval between keepalive probes
        --key <key>     Private key file name (SSL/SSH)
        --key-type <type> Private key file type (DER/PEM/ENG) (SSL)
        --krb <level>   Enable Kerberos with specified security level (F)
        --libcurl <file> Dump libcurl equivalent code of this command line
        --limit-rate <rate> Limit transfer speed to this rate
     -l/--list-only     List only names of an FTP directory (F)
        --local-port <num>[-num] Force use of these local port numbers
     -L/--location      Follow Location: hints (H)
        --location-trusted Follow Location: and send auth to other hosts (H)
     -M/--manual        Display the full manual
        --max-filesize <bytes> Maximum file size to download (H/F)
        --max-redirs <num> Maximum number of redirects allowed (H)
     -m/--max-time <seconds> Maximum time allowed for the transfer
        --negotiate     Use HTTP Negotiate Authentication (H)
     -n/--netrc         Must read .netrc for user name and password
        --netrc-optional Use either .netrc or URL; overrides -n
     -N/--no-buffer     Disable buffering of the output stream
        --no-keepalive  Disable keepalive use on the connection
        --no-sessionid  Disable SSL session-ID reusing (SSL)
        --noproxy       Comma-separated list of hosts which do not use proxy
        --ntlm          Use HTTP NTLM authentication (H)
     -o/--output <file> Write output to <file> instead of stdout
        --pass  <pass>  Pass phrase for the private key (SSL/SSH)
        --post301       Do not switch to GET after following a 301 redirect (H)
        --post302       Do not switch to GET after following a 302 redirect (H)
     -#/--progress-bar  Display transfer progress as a progress bar
     -x/--proxy <host[:port]> Use HTTP proxy on given port
        --proxy-anyauth Pick "any" proxy authentication method (H)
        --proxy-basic   Use Basic authentication on the proxy (H)
        --proxy-digest  Use Digest authentication on the proxy (H)
        --proxy-negotiate Use Negotiate authentication on the proxy (H)
        --proxy-ntlm    Use NTLM authentication on the proxy (H)
     -U/--proxy-user <user[:password]> Set proxy user and password
        --proxy1.0 <host[:port]> Use HTTP/1.0 proxy on given port
     -p/--proxytunnel   Operate through a HTTP proxy tunnel (using CONNECT)
        --pubkey <key>  Public key file name (SSH)
     -Q/--quote <cmd>   Send command(s) to server before file transfer (F/SFTP)
        --random-file <file> File for reading random data from (SSL)
     -r/--range <range> Retrieve only the bytes within a range
        --raw           Pass HTTP "raw", without any transfer decoding (H)
     -e/--referer       Referer URL (H)
     -O/--remote-name   Write output to a file named as the remote file
        --remote-name-all Use the remote file name for all URLs
     -R/--remote-time   Set the remote file's time on the local output
     -X/--request <command> Specify request command to use
        --retry <num>   Retry request <num> times if transient problems occur
        --retry-delay <seconds> When retrying, wait this many seconds between each
        --retry-max-time <seconds> Retry only within this period
     -S/--show-error    Show error. With -s, make curl show errors when they occur
     -s/--silent        Silent mode. Don't output anything
        --socks4 <host[:port]> SOCKS4 proxy on given host + port
        --socks4a <host[:port]> SOCKS4a proxy on given host + port
        --socks5 <host[:port]> SOCKS5 proxy on given host + port
        --socks5-hostname <host[:port]> SOCKS5 proxy, pass host name to proxy
        --socks5-gssapi-service <name> SOCKS5 proxy service name for gssapi
        --socks5-gssapi-nec  Compatibility with NEC SOCKS5 server
     -Y/--speed-limit   Stop transfer if below speed-limit for 'speed-time' secs
     -y/--speed-time    Time needed to trig speed-limit abort. Defaults to 30
     -2/--sslv2         Use SSLv2 (SSL)
     -3/--sslv3         Use SSLv3 (SSL)
        --stderr <file> Where to redirect stderr. - means stdout
        --tcp-nodelay   Use the TCP_NODELAY option
     -t/--telnet-option <OPT=val> Set telnet option
     -z/--time-cond <time> Transfer based on a time condition
     -1/--tlsv1         Use TLSv1 (SSL)
        --trace <file>  Write a debug trace to the given file
        --trace-ascii <file> Like --trace but without the hex output
        --trace-time    Add time stamps to trace/verbose output
     -T/--upload-file <file> Transfer <file> to remote site
        --url <URL>     Set URL to work with
     -B/--use-ascii     Use ASCII/text transfer
     -u/--user <user[:password]> Set server user and password
     -A/--user-agent <string> User-Agent to send to server (H)
     -v/--verbose       Make the operation more talkative
     -V/--version       Show version number and quit
     -w/--write-out <format> What to output after completion
     -q                 If used as the first parameter disables .curlrc

