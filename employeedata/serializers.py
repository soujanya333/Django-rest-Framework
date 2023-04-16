from rest_framework import serializers
import ast
        
        
class EmployeeSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "name":instance.name,
            "email": instance.email,
            "age": instance.age,
            "gender": instance.gender,
            "phoneNo": instance.phone_no,
            "addressDetails":ast.literal_eval(instance.address_details),
            "workExeperience":ast.literal_eval(instance.work_exeperience),
            "qualifications":ast.literal_eval(instance.qualifications),
            "photo":instance.photo
            
        }
        
        
def check_validate(body):
    if body.get('email') == "" or body.get("regid") == "" or body.get("phoneNo") == "":
        return False
    else:
        return True
