from .models import Post
from django.core.cache import cache
from django.http import JsonResponse


def add_posts(request):
    bulk_list = []
    for i in range(1, 1001):
        t = "Test Post: {}".format(i)
        c = "This is the test post {}".format(i)
        bulk_list.append(Post(title=t, content=c))

    Post.objects.bulk_create(bulk_list)
    return JsonResponse({'message': 'good'})


def show_posts(request):
    posts = Post.objects.all()
    dic = {}
    for post in posts:
        dic[post.title] = post.content
    return JsonResponse(dic, safe=False)


def show_posts_redis(request):
    posts = cache.get('posts')

    if not posts:
        posts = {}
        p = Post.objects.all()
        for post in p:
            posts[post.title] = post.content
        cache.set('posts', posts)

    return JsonResponse(posts, safe=False)