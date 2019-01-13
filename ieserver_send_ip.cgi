#!/usr/bin/perl

## 最終更新: 9 Jan, 2011

## 設定ここから

#ユーザー名(ieserver.net)
$username = '';

#パスワード(ieserver.net)
$password = '';

#サブドメイン名(ieserver.net)
$domain = 'moe.hm';

## 設定ここまで

use LWP::UserAgent;

#LWP作成
$ua = LWP::UserAgent->new;
$url = 'http://ieserver.net:80/cgi-bin/dip.cgi';
$query_string = "username=$username&password=$password&domain=$domain&updatehost=Go";

#リクエスト作成
$req = HTTP::Request->new(POST => $url);
$req->content_type('application/x-www-form-urlencoded');
$req->content($query_string);

#リクエスト送信
$res = $ua->request($req);
print "Content-type: text/plain\n\n";
print $res->as_string;	#出力

1;