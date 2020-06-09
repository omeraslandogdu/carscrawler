from rest_framework import viewsets


class CommentRatingModelViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
