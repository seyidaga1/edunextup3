from rest_framework import generics, permissions ,exceptions
from accounts.models import Profile
from .serializers import ProfileSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:  # Check if the user is logged in
            return user.profile
        return exceptions.AuthenticationFailed('You need to log in.')
