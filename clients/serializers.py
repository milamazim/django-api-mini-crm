from rest_framework import serializers
from clients.models import Client

class ClientSerializer(serializers.ModelSerializer):

    def validate_tax_id(self, value):
        queryset = Client.objects.filter(tax_id=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Client with this tax_id already exists.")

        return value

    
    class Meta:
        model = Client
        fields = [
            'id',
            'company_name',
            'tax_id',
            'contact_name',
            'contact_email',
            'contact_phone',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
