from rest_framework import viewsets

from library.models import Book, Borrowing
from library.serializers import BookSerializer, BorrowingSerializer, BorrowingListSerializer, BorrowingDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BorrowingDetailSerializer

        if self.action == "list":
            return BorrowingListSerializer

        return BorrowingSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == ("list", "retrieve"):
            queryset = Borrowing.objects.select_related("book")

        return queryset
