# -*- coding: utf-8 -*-
import json
import time
import datetime
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render


from .wyy_music import *
from .models import *
from .Uid import *
# Create your views here.




# json时间处理
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')   
        elif isinstance(obj,date):
            return obj.strftime('%Y-%m-%d')
        else:    
            return json.JSONEncoder.default(self, obj) 


# 通用函数,返回json数据
def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp,cls=DateEncoder), content_type='application/json')


# 映射主页
def index(request):
    return render(request, 'index.html')

# 详情页面
def details_html(request):
    return render(request, 'details_html.html')


# 搜索id API
def music_id(request):
    if request.method != 'POST': # 必须POST 请求 负责返回 Method not allowed
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errorMsg = 'Method not allowed',successResult='',uid = ''))

    mic_id = request.POST.get('mic_id',None)    # 获取POST提交的 mic_id   (个人id)
    if not mic_id:  # mic_id为空 返回 Please upload parameters mic_id
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Please upload parameters mic_id',successResult='',uid = ''))
    
    uid = Uid()   # 生成唯一标识uid
    try:
        res = song_all(mic_id,uid)
        res_s = song_week(mic_id,uid)
        if res == 'err':
            return get_json_response(request, dict(suc_id=1, ret_cd=500, ret_ts=long(time.time()),errorMsg = 'err,There is no data ',successResult='',uid = ''))
        return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()),errorMsg = '',successResult=res,uid = uid))
    except Exception, err:
        return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()),errorMsg = 'err',successResult='',uid = ''))


# 检索结果集并返回 参数 uid
def music_uid_data(request):
    if request.method != 'POST': # 必须POST 请求 负责返回 Method not allowed
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errorMsg = 'Method not allowed',successResult='',uid = ''))

    uid = request.POST.get('uid',None) # 获取POST 获取的 uid
    if not uid: # 如果uid不存在  返回 Please upload parameters mic_id
       return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Please upload parameters mic_id',successResult='',uid = ''))
     
    music_data = [] 
    mus = MUSIC.objects.filter(star_id = uid)   # 根据uid查找数据
    if not mus: # 如果不存在数据 返回 There is no data
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'There is no data',successResult='',uid = ''))
    for _ in mus:
        song_name = _.song_name
        singer = _.singer
        frequency = _.frequency
        mis_id = _.mis_id
        star_id = _.star_id
        music_list = {
           'song_name':song_name,'singer':singer,'frequency':frequency,'mis_id':mis_id,'star_id':star_id
        }
        music_data.append(music_list)
    return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()),errorMsg = '',successResult=music_data,uid = uid))
