# curl

HTTPリクエスト コマンド

## GET

`$ curl localhost/ctf/question`

## ファイルに出力

`$ curl localhost/ctf/question -o aaa.txt`

-O でリクエスト先の名前でファイル保存

`$ curl localhost/ctf/question -O
$ cat question`

## HTTP Headerを確認する

### -I Headerのみ

`$ curl localhost/ctf/question -I`

### -i Header, Body 両方

`$ curl localhost/ctf/question -i`

### -v リクレストHeaderも

`$ curl localhost/ctf/question -v`

## POST

    $ curl -i localhost/ctf/question/1 -X POST --data 'flag=sasakama@matsushima'
    HTTP/1.1 302 Found
    Date: Tue, 09 Jan 2018 07:39:55 GMT
    Server: Apache-Coyote/1.1
    Location: http://10.132.83.231/ctf/question/1/good
    Content-Language: ja-JP
    Content-Length: 0
    Set-Cookie: JSESSIONID=D0DAB5A78F64098D59282AAE1954DA24; Path=/ctf/; HttpOnly
    Connection: close
    Content-Type: text/plain; charset=UTF-8


