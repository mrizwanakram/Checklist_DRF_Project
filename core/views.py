from core.models import CheckList, CheckListItem
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import ChecklistSerializer, ChecklistItemSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({'name': 'adeel'})

class CheckListApiView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, format=None):
        data = CheckList.objects.all()
        serializer = ChecklistSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ChecklistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckListAPIView(APIView):
    serializer_class = ChecklistSerializer

    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404("CheckList not found")

    def get(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CheckListItemCreateAPIView(APIView):
    serializer_class = ChecklistItemSerializer
    def post(self,request, format= None):
        serializer = ChecklistItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListItemAPIView(APIView):
    serializer_class = ChecklistItemSerializer
    def get_object(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404("CheckListItem not found")
        
    def get(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# Genric Api Views Code

# class CheckListApiView(ListCreateAPIView):
#     permission_classes = [IsAuthenticated, IsOwner]
#     def get_queryset(self):
#         queryset = CheckList.objects.filter(user = self.request.user)
#         return queryset

# class CheckListAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ChecklistSerializer
#     permission_classes = [IsAuthenticated, IsOwner]

#     def get_queryset(self):
#         queryset = CheckList.objects.filter(user = self.request.user)
#         return queryset


# class CheckListItemCreateAPIView(CreateAPIView):
#     serializer_class = ChecklistItemSerializer
#     permission_classes = [IsAuthenticated, ]


# class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated, IsOwner]
#     serializer_class = ChecklistItemSerializer

#     def get_queryset(self):
#         queryset = CheckListItem.objects.filter(user = self.request.user)
#         return queryset