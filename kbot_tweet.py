#!/usr/bin/env python
#coding:utf-8

from requests_oauthlib import OAuth1Session
import key,twt_cntnts,random

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"
# twt_cntntsからツイートを取得する為のキー生成
def CreateRDMKey():
	return random.randint(1,10)

rdm_key = CreateRDMKey
# ツイート本文
params = {"status": twt_cntnts.twt(CreateRDMKey)}

# ツイートの重複をチェック
def twt_OverlapCheck(twt):
	if twt == twt_list[-1]:
		rdm_key = CreateRDMKey
	else:
		twt_list = append(rdm_key)

	#twt_list の最大値を3に維持
	if max(twt_list) == 1:
		twt_list = []

	return twt


# OAuth認証で POST method で投稿
twitter = OAuth1Session(key.CK, key.CS, key.AT, key.AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)