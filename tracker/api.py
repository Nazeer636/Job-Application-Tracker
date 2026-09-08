from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = [
            'id',
            'company',
            'role',
            'applied_date',
            'interview_date',
            'status',
            'job_url',
            'notes',
            'created_at',
        ]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404


class JobApplicationListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = JobApplication.objects.filter(user=request.user)

        serializer = JobApplicationSerializer(jobs, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class JobApplicationDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        return get_object_or_404(
            JobApplication,
            pk=pk,
            user=request.user
        )

    def get(self, request, pk):
        job = self.get_object(request, pk)

        serializer = JobApplicationSerializer(job)

        return Response(serializer.data)

    def put(self, request, pk):
        job = self.get_object(request, pk)

        serializer = JobApplicationSerializer(
            job,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        job = self.get_object(request, pk)

        serializer = JobApplicationSerializer(
            job,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        job = self.get_object(request, pk)

        job.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )