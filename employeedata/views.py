from .models import EmployeeData
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, check_validate
from rest_framework.response import Response


# Create your views here.


class EmployeeList(APIView):

    def get(self,request):
        """
        logic for Single employee details by giving regid
        else all the employee records

        url :http://127.0.0.1:8000/api/getall?regid=EMP001234
        """
        
        try:
            #fecth then id from the request and
            #check is user not given id if block if fetch the all records from db
            id = request.GET.get('regid')
            if id == None:
                employee_data= EmployeeData.objects.all()
                print(employee_data)
                serializer = EmployeeSerializer(employee_data, many=True)
                result = {
                    "message":"employee details found",
                    "success":True,
                    "employees":serializer.data
                }
                #return Response(result)
            else:
                #if id is persent it will fecth the respective record
                snippets = EmployeeData.objects.get(regid=id)
                if snippets:
                        serializer = EmployeeSerializer(snippets)
                        result = {
                            "message":"employee details found",
                            "success":True,
                            "employees":serializer.data
                        }
                        #return Response(res)
            
            return Response(result)
        except Exception as err:
            return Response({
                        "message":"employee details found",
                        "success":True,
                        "employees":[]
                    })
            
        
    def post(self, request):
        """
        logic for employye creation

        url :http://127.0.0.1:8000/api/getall
        """
        try:
            data = request.data
            #check with email any record is present if present ignore
            #to save the data in db
            check_email = EmployeeData.objects.filter(email=data.get('email'))
            if check_email:
                result = {
                    "message":"employe already exist",
                    "success":False,
                    "status_code":200
                    }
            else:
                #validate each field in json body  request not an empty 
                #validation is applied for email, regid, PhoneNo
                data_validation  = check_validate(data)
                if data_validation:
                    employee_data = EmployeeData(
                    name = data.get('name'),
                    email = data.get('email'),
                    age = data.get('age'),
                    gender = data.get('gender'),
                    phone_no = data.get('phoneNo'),
                    address_details= dict(data.get('addressDetails')),
                    work_exeperience = list(data.get('workExperience')),
                    qualifications = list(data.get('qualifications')),
                    projects= list(data.get('projects')),
                    photo = data.get('photo'),
                    regid = data.get('regid')
                    )
                    employee_data.save()
                    result = {
                        "message":"employee created successfully",
                        "success":True
                        }
                else:
                    result  = {
                        "message":"invalid body request",
                        "sucess":False}
                
            return Response(result)
        except Exception as err:
            return Response({
                "message":"employee created failed",
                "success":False,
                "status_code":500}
                            )

   
   
   
   
class  UpdateEmployee(APIView):         
    def post(self,request):
        """
        logic for update an employee using regid

        url :http://127.0.0.1:8000/api/updateemployee?regid=EMP001234
        """
        try:
            #update the record with the given regid
            data = request.data
            regid = request.GET.get('regid')
            #check the regid record present in table if yes validate the request body to update
            if EmployeeData.objects.filter(regid=regid):
                res1 = check_validate(data)
                if res1:
                    update_employee = EmployeeData.objects.get(regid=regid)
                    update_employee.name = data.get('name')
                    update_employee.email = data.get('email')
                    update_employee.age= data.get('age')
                    update_employee.gender= data.get('gender')
                    update_employee.phone_no = data.get('phoneNo')
                    update_employee.address_details = str(data.get('addressDetails'))
                    update_employee.work_exeperience= str(data.get('workExperience'))
                    update_employee.qualifications= str(data.get('qualifications'))
                    update_employee.projects = str(data.get('projects'))
                    update_employee.photo = data.get('photo')
                    update_employee.save()
                    result = {
                        "message":"employee details updated successfully",
                        "success":True,
                        "status_code":200
                        }
                else:
                    result = {
                    "message":"invalid body request",
                    "sucess":False,
                    "status_code":400
                    }
                
            else:
                result = {
                    "message":"no employee found with this regid",
                    "success":False,
                    "status_code":200
                }
            return Response(result)
        except Exception as err:
            return Response({
                "message":"employee updation failed”",
                "success":False,
                "status_code":500}
            )
    
    def delete(self, request):
        try:
            #check the request json body is valid or not
            data = request.data
            if data.get('regid') == "":
                result = {"message":"invalid body request",
                                "success":False,
                                "status_code":400}
            else:
                #if record exist record will delete 
                delete_record = EmployeeData.objects.filter(regid=data.get('regid'))
                if delete_record:
                        delete_record.delete()
                        result = {"message":"employee deleted successfully",
                                        "success":True,
                                        "status_code":200
                                        }
                else:
                    result = {"message":"no employee found with this regid",
                                "success":False,
                                "status_code":200}
            return Response(result)
        
        except Exception as err:
            return Response({
                "message":"employee created failed",
                "success":False,
                "status_code":500}
                            )


