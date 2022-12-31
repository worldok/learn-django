from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
# class StudentForm(forms.Form):
    # name = forms.CharField(lable='姓名', max_lenght=128)
    # sex = forms.ChoiceField(lable='性别', choices=Student.SEX_ITEMS)
    # profession = forms.CharField(label='职业', max_lenght=128)
    # email = forms.EmailField(label='邮箱', max_length=128)
    # qq = forms.CharField(lable='QQ', max_leght=128)
    # phone = forms.CharField(lable='手机', max_lenght=128)

    # 复用model代码
    # 验证QQ必须是数字 其他字段验证可以修改方法名替代
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            # 返回错误信息
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)
    class Meta:
        model = Student
        fields = {
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        }

