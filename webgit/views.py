import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def processPayload(payload):
    logger = logging.getLogger("webgit.views.processPayload")
    try:
      data = json.loads(request.POST['payload'])
    except:
      logger.info("payload probably malformed")
      return False
    pusher_name = data['pusher']['name']
    repo_name = data['repository']['name']
    logger.info("%s pushed to repository %s"%(pusher_name, repository_name))
    return True


#@require_http_methods(["POST",])
@csrf_exempt
def webhook(request):
  """
  {u'payload': [u'{"pusher":{"name":"none"},"repository":{"name":"angryplanet","created_at":"2011-12-28T07:54:46-08:00","size":23004,"has_wiki":true,"private":false,"watchers":0,"language":"Python","url":"https://github.com/aneumeier/angryplanet","fork":false,"id":3063477,"pushed_at":"2012-09-19T11:39:14-07:00","has_downloads":true,"open_issues":10,"has_issues":true,"homepage":"","description":"","forks":0,"stargazers":0,"owner":{"name":"aneumeier","email":"andreas@neumeier.org"}},"forced":false,"after":"94e23e310a2068f755b6e3afc75004c80d5507b2","head_commit":{"added":[],"modified":["README.md"],"timestamp":"2012-09-19T11:38:57-07:00","removed":[],"author":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"},"url":"https://github.com/aneumeier/angryplanet/commit/94e23e310a2068f755b6e3afc75004c80d5507b2","id":"94e23e310a2068f755b6e3afc75004c80d5507b2","distinct":true,"message":"changed readme","committer":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"}},"deleted":false,"ref":"refs/heads/master","commits":[{"added":["password/templates/password/websiteup.html"],"modified":[".travis.yml","requirements.txt"],"timestamp":"2012-09-10T02:11:45-07:00","removed":[],"author":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"},"url":"https://github.com/aneumeier/angryplanet/commit/c6049df5099d7aecd6e08bbe618d9740d0574709","id":"c6049df5099d7aecd6e08bbe618d9740d0574709","distinct":true,"message":"use django-ilike package to install \'star\'","committer":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"}},{"added":["krippen/__init__.py","krippen/admin.py","krippen/models.py","krippen/tests.py","krippen/views.py","tests.py","userprofile/fields.py","userprofile/templatetags/__init__.py","userprofile/templatetags/gravatar.py"],"modified":["feeds/tools.py","feeds/update.py","feeds/views.py","scrum/models.py","settings.py","templates/index.html"],"timestamp":"2012-09-19T11:33:44-07:00","removed":[],"author":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"},"url":"https://github.com/aneumeier/angryplanet/commit/a862841029d0f17e49e786e0614f3c99b928803b","id":"a862841029d0f17e49e786e0614f3c99b928803b","distinct":true,"message":"cleaned up","committer":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"}},{"added":[],"modified":["README.md"],"timestamp":"2012-09-19T11:38:57-07:00","removed":[],"author":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"},"url":"https://github.com/aneumeier/angryplanet/commit/94e23e310a2068f755b6e3afc75004c80d5507b2","id":"94e23e310a2068f755b6e3afc75004c80d5507b2","distinct":true,"message":"changed readme","committer":{"name":"Andreas Neumeier","username":"aneumeier","email":"andreas@neumeier.org"}}],"compare":"https://github.com/aneumeier/angryplanet/compare/bbac1ed31718...94e23e310a20","before":"bbac1ed3171808302dae259f8e1cf09b89d18160","created":false}']}
  """
  logger = logging.getLogger("webgit.views.webhook")
  if request.method == 'POST':
    if request.META['REMOTE_ADDR'] in ["207.97.227.253", "50.57.128.197", "108.171.174.178", "127.0.0.1"]:
      if "payload" in request.POST:
        result = processPayload(request.POST['payload'])
        if result:
          return HttpResponse(status=200)
      else:
        logger.debug("request didn't have a payload")
        return HttpResponse(status=400)

    else:
      logger.debug("other post")
      return HttpResponse(status=400)
  else:
    return HttpResponse("GET", status=200)

