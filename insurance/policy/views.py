from django.shortcuts import render
import requests
import csv, time
from dateutil import parser

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from .models import Policy
from .serializers import PolicySerializer


from django.shortcuts import render


def index(request):
    """ Function based index view. """
    return render(request, 'index.html', {
        'key': "val"
    })


def policy_details(request):
    """Policy Details."""
    return render(request, 'policy_details.html', {
        'key': "val"
    })


def policy_chart(request):
    """ Policy Bar Chart Info. """
    return render(request, 'policy_chart.html', {
        'key': "val"
    })


def policy_add(request):
    """ Policy add. """
    return render(request, 'policy_add.html', {
        'key': "val"
    })


def policy_edit(request):
    """ Policy edit. """
    return render(request, 'policy_edit.html', {
        'key': "val"
    })


class PolicyAdd(generics.GenericAPIView):
    """ Class based Policy Bulk Add API. """
    serializer_class = PolicySerializer

    def post(self, request):
        try:
            serializer = PolicySerializer(data=request.data, context={'request': request})
            if not serializer.is_valid():
                # raise Exception("Error: Invalid request payload data.")
                pass
            request_payload = serializer.data
            csv_file_path = "policy.csv"
            with open(csv_file_path, ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    policy_obj = Policy(Policy_id=row['Policy_id'], Date_of_Purchase=row['Date of Purchase'], Customer_id=row['Customer_id'], Fuel=row['Fuel'],
                                          VEHICLE_SEGMENT=row['VEHICLE_SEGMENT'], Premium=row['Premium'],
                                        bodily_injury_liability=row['bodily injury liability'], personal_injury_protection=row[' personal injury protection'],
                                          property_damage_liability=row[' property damage liability'], collision=row[
                            ' collision'], comprehensive=row[' comprehensive'], Customer_Gender=row['Customer_Gender'],
                                          Customer_Income_group=row['Customer_Income group'], Customer_Region=row['Customer_Region'], Customer_Marital_status=row['Customer_Marital_status'])
                    policy_obj.save()

            msg = "Successfully Generated climate csv."
            return Response({"response": msg}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Bad request. Error {e}", status=status.HTTP_400_BAD_REQUEST)


class PolicyListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PolicySerializer
    queryset = Policy.objects.all().order_by('id')

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PolicyChartAPI(APIView):

    def str_to_date(self, str_date):
        return parser.parse(str_date).strftime("%B")


    def get(self, request, format=None):

        policy_by_month = {"January":0, "February":0, "March":0, "April":0, "May":0, "June":0, "July":0, "August":0,
                            "September":0,  "October":0, "November":0, "December":0}

        policy_obj = Policy.objects.all()
        serializer = PolicySerializer(policy_obj, context={'request': request}, many=True)
        serializer_objs = serializer.data

        for serializer_obj in serializer_objs:
            date_of_purchase = serializer_obj["Date_of_Purchase"]
            # policy_id = serializer_obj["Policy_id"]
            # customer_region = serializer_obj["Customer_Region"]
            purchase_month = self.str_to_date(date_of_purchase)
            if purchase_month in policy_by_month:
                policy_count = policy_by_month.get(purchase_month, 0)
                policy_by_month.update({purchase_month: policy_count+1})
                policy_count = 0
        months_x, policy_y = zip(*policy_by_month.items())
        response_data = {"x_axis": months_x, "y_axis": policy_y}
        return Response(response_data)


class PolicySearchAPI(APIView):
    """ Policy Search by Customer / Policy ID  API"""
    def get(self, request, cid=None, pid=None, format=None):
        cid = request.GET.get('cid', None)
        pid = request.GET.get('pid', None)
        if cid:
            policy_obj = Policy.objects.filter(Customer_id=cid)
        elif pid:
            policy_obj = Policy.objects.filter(Policy_id=pid)
        else:
            policy_obj = Policy.objects.all()
            pass
        serializer = PolicySerializer(policy_obj, context={'request': request}, many=True)
        return Response(serializer.data)


class PolicyDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    """ Policy Read Update Delete API"""

    serializer_class = PolicySerializer
    queryset = Policy.objects.all()
    lookup_field = 'id'

    def get(self, request, id=id):

        return self.retrieve(request, id)

    def put(self, request, id=id):
        return self.update(request, id)

    def delete(self, request, id=id):
        return self.destroy(request, id)
