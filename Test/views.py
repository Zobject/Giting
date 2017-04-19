from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from Test.models import Test
#from Test.serializers import SnippetSerializer

import json
from bson import json_util,ObjectId
import pymongo

try:
    conn=pymongo.MongoClient()
    print "success"
except pymongo.errors.ConnectionFailure,e:
    print "error %s"%e


db=conn['Mmcalculator']
collection=db.my_collection

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method=='GET':
        for d in  collection.find():
            data=list(collection.find())
            return JsonResponse(json.dumps(data,default=json_util.default),safe=False)
    elif request.method == 'POST':
            data = JSONParser().parse(request)
            #print data
            user=data.get("usr")
            photourl=data.get("photourl")
            if photourl==None:
                print "none"
                data=list(collection.find({"usr":user}))
                print data
                return JsonResponse(json.dumps(data,default=json_util.default),safe=False,status=201)

            else:
                data = {"usr":user,"photourl":photourl}
                #abc = data.get("name")
                #print abc

                print data
                collection.insert(data)
                return JsonResponse({"ok":1})
            #return JsonResponse(json.dumps(data,default=json_util.default),safe=False,status=201)

    elif request.method =='DELETE':
        data=JSONParser.parse(request)
        id=data.get('id')
        print id
        collection.remove({"_id":ObjectId(id)})
        return HttpResponse(status=204)
    return JsonResponse(status=404)

        # @csrf_exempt
# def snippet_detail(request,id):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = list(collection.find({"id":id}))
#     except snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#
#         return JsonResponse(json.dumps(snippet,default=json_util.default),safe=False)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         print "++++++++"
#         print data
#         id=data.get("id")
#         name=collection.find({"_id":ObjectId(id)})
#         data1=json.dumps(name.next(),default=json_util.default)
#         #_id=data1.get("_id")
#         #print str(_id)
#         #print json.dumps({""})
#
#         return JsonResponse(data1,safe=False)
#
#     elif request.method == 'DELETE':
#         data=JSONParser.parse(request)
#         info=data.get('id')
#         collection.remove({"id":info})
#         return HttpResponse(status=204)