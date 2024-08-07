from rest_framework import serializers
from core.models import CheckList, CheckListItem

   

class ChecklistItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = CheckListItem
        fields = '__all__'
    
class ChecklistSerializer(serializers.ModelSerializer):
    items = ChecklistItemSerializer(source = 'checklistitem_set', many = True, read_only = True)
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = CheckList
        fields = '__all__'
 