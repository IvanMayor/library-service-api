from rest_framework import serializers

from library.models import Book, Borrowing


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "cover",
            "inventory",
            "daily_fee"
        )


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return",
            "actual_return",
            "book",
            "user",
        )


class BorrowingListSerializer(BorrowingSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=True, slug_field="title")
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field="email")


class BorrowingDetailSerializer(BorrowingSerializer):
    book = BookSerializer(many=False, read_only=True)
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field="email")
