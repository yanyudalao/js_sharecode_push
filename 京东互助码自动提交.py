import requests

# 东东工厂互助码：
ddgc = ['P04z54XCjVWnYaS5u2Ghrh2UwU26townPin','P04z54XCjVWnYaS5jEKD2D62HhJiP2UsxzsLw','P04z54XCjVWnYaS5uGApLVbSKjCKOQObABNrig']
ddgc_hzurl = 'http://api.turinglabs.net/api/v1/jd/ddfactory/create/'
ddgc_ckurl = 'http://api.turinglabs.net/api/v1/jd/ddfactory/count/'

# 惊喜工厂：
jxgc = ['4Mw1dfgR17YgbeGRzDh2zA==','DF-bIzGkHD-cpvLfq4nqrQ==']
jxgc_hzurl = 'http://api.turinglabs.net/api/v1/jd/jxfactory/create/'
jxgc_ckurl = 'http://api.turinglabs.net/api/v1/jd/jxfactory/count/'

# 种豆得豆互助码：
zddd = ['qkvflbyz2sjkccr3oavvxdmksnzo5usmp3gyvti','w2ipph4dz63qfmwsa4pelabsepgallaelnodbfq','qe7gzkbroeiqdaomid3p6u6glzfnfb7dhn6q22y']
zddd_hzurl = 'http://api.turinglabs.net/api/v1/jd/bean/create/'
zddd_ckurl = 'http://api.turinglabs.net/api/v1/jd/bean/count/'

# 农场互助码：
nchz = ['c570df972a1e46c3ab62670709ab3fb8','d12d761f945d41f49ef38c399bc909e9','1ae95a3dd1fc440ca3e59cc5e9580ad9']
nchz_hzurl = 'http://api.turinglabs.net/api/v1/jd/farm/create/'
nchz_ckurl = 'http://api.turinglabs.net/api/v1/jd/farm/count/'

# 宠物互助码
cwhz = ['MTE1NDAxNzgwMDAwMDAwNDA5Mzk3NzE=','MTE1NDAxNzcwMDAwMDAwNDExNTYwNDE=','MTE1NDUyMjEwMDAwMDAwNDIxMDcyMDU=']
cwhz_hzurl = 'http://api.turinglabs.net/api/v1/jd/pet/create/'
cwhz_ckurl = 'http://api.turinglabs.net/api/v1/jd/pet/count/'

#查看数据库清空时间
qktime_url = 'http://api.turinglabs.net/api/v1/jd/cleantimeinfo/'


all_get_hzm = [ddgc,jxgc,zddd,nchz]
all_get_url = [ddgc_hzurl,jxgc_hzurl,zddd_hzurl,nchz_hzurl]
all_ck_url = [ddgc_ckurl,jxgc_ckurl,zddd_ckurl,nchz_ckurl]
for i in all_get_url:
    hit = all_get_url.index(i)
    for j in all_get_hzm[hit]:
        url = i+j
        print(requests.get(url).text)
    print(requests.get(all_ck_url[hit]).text)
    print('-------------------')

