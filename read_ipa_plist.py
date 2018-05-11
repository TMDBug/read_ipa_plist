#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import os
import sys
import time
import plistlib

# 配置：ipa_path: ipa包的绝对路径
ipa_path="/YOUR/IPA/PATH/XXXXXXXXXX2018-05-10-17-43-13"
# ipa_name：ipa文件的名字(不带后缀)
ipa_name="XXXXXXXXXX"

def read_plist():
	os.system('cp %s/%s.ipa %s/%s.zip' % (ipa_path, ipa_name, ipa_path, ipa_name))
	os.system('unzip %s/%s.zip' % (ipa_path, ipa_name))
	plist_path = '%s/Payload/%s.app/Info.plist' % (ipa_path, ipa_name)
	f = open(plist_path,'rb');
	plist_data = f.read()
	plist = plistlib.loads(plist_data)
	print(plist)
	
def run():
	read_plist()
	
# - 开始执行 -
run()
