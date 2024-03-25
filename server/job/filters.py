from django_filters import rest_framework as filters
from .models import Job


class JobsFilter(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name="salary" or 0, lookup_expr="gte")
    max_salary = filters.NumberFilter(field_name="salary" or 1000000, lookup_expr="lte")
    # Keyword and location will be filtered not by exactly a title but if word is contained in a title
    keyword = filters.CharFilter(field_name="title", lookup_expr="icontains")
    location = filters.CharFilter(field_name="address", lookup_expr="icontains")

    class Meta:
        model = Job
        fields = [
            "education",
            "industry",
            "experience",
            "jobType",
            "min_salary",
            "max_salary",
            "keyword",
            "location",
        ]
