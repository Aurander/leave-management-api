from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import LeaveRequest
from .serializers import LeaveSerializer

# Employee: Apply + View own leave


class LeaveListCreateView(generics.ListCreateAPIView):
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Admin: Approve / Reject
class LeaveUpdateView(generics.UpdateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAdminUser]
