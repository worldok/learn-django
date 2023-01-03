from django.test import TestCase, Client

# Create your tests here.
from .models import Student


class StudentTestCase(TestCase):
    # 初始化环境 创建初始化数据
    def setUp(self):
        Student.object.create(
            name='the5fire',
            sex=1,
            email='nobody@the5fire.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )

    # test_xxxx(self):后面xxxx可以是任意东西，以test_开头的方法会被认为需要测试的方法，跑测试会被执行
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang1',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟显示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='huyang2',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='333',
            phone='32222',
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 302!')

    def test_post_student(self):
        client = Client()
        data = dict(
            ame='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='程序员',
            qq='333',
            phone='32222',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('')
        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain `test_for_post`')
