from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serizliers import LinkSerializer
from .models import Link


class PostListApi(ListAPIView):
	model = Link

class PostCreateApi(CreateAPIView):
	queryset = Link.objects.filter(active=True)
	serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
	queryset = Link.objects.filter(active=True)
	serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView
):
	queryset = Link.objects.filter(active=True)
	serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
	queryset = Link.objects.filter(active=True)
	serializer_class = LinkSerializer