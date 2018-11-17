# by luffycity.com

from rest_framework import serializers

from app01.models import *
# 为queryset,model对象做序列化
class PublishSerializers(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()


class PublishModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publish
        fields="__all__"




# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField()
#     publish=serializers.CharField(source="publish.name")
#     #authors=serializers.CharField(source="authors.all")
#     authors = serializers.SerializerMethodField()
#     def get_authors(self,obj):
#         temp=[]
#         for obj in obj.authors.all():
#             temp.append(obj.name)
#         return temp

'''
序列化BookSerializers(book_list,many=True)过程：
     temp=[]
     for obj in book_list:
         temp.append({
            "title":obj.title,
            "price":obj.price,
            "pub_date":obj.pub_date,
            "publish":str(obj.publish), # obj.publish.name
            #"authors":obj.authors.all,
            "authors": get_authors(obj)
         })

'''


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    #publish=serializers.CharField(source="publish.pk")
    publish=serializers.HyperlinkedIdentityField(
            view_name="detailpublish",
            lookup_field="publish_id",
            lookup_url_kwarg="pk",

    )


    # authors=serializers.CharField(source="authors.all")
    # authors = serializers.SerializerMethodField()
    # def get_authors(self,obj):
    #     temp=[]
    #     for obj in obj.authors.all():
    #         temp.append(obj.name)
    #     return temp

    def create(self, validated_data):
        print("validated_data",validated_data)
        book=Book.objects.create(title=validated_data["title"],price=validated_data["price"],pub_date=validated_data["pub_date"],publish_id=validated_data["publish"]["pk"])
        book.authors.add(*validated_data["authors"])

        return book


class AuthorModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"