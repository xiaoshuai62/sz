import json
class StudentMessage:
    def __init__(self,name : str,chinese : float,math : float,english : float):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english
    def __str__(self) -> str:
        return f"姓名:{self.name} \t | \t 语文:{self.chinese} \t | \t 数学:{self.math} \t | \t 英语:{self.english} \t | \t 总分:{self.total}"
class EducationManagement:
    def __init__(self):
        self.system = {}
    def r_json(self):
        with open("学生信息.json","r",encoding="utf-8") as f:
            self.system = json.load(f)
    def w_json(self):
        with open("学生信息.json","w",encoding="utf-8") as f:
            json.dump(self.system,f,ensure_ascii=False,indent=2)
    def input_score(self,subject):
        while True:
            try:
                score = float(input(f"请输入{subject}成绩:"))
                if score < 0 or score > 100:
                    print("输入的学生成绩必须在0~100的区间内,请重新输入:")
                    continue
                else:
                    return score
            except ValueError:
                print("请输入(0~100)的数字!")
    def add_student(self):
        try:
            name = input("请输入要添加的学生姓名:")
            self.r_json()
            if name in self.system:
                print(f"{name}已经在教务系统中了,添加失败!")
            else:
                chinese = self.input_score("语文")
                math = self.input_score("数学")
                english = self.input_score("英语")
                self.system[name] = {
                    "姓名" : name,
                    "语文" : chinese,
                    "数学" : math,
                    "英语" : english,
                    "总分" : chinese + math + english
                }
                self.w_json()
                print(f"{name}的信息添加成功~")
                student = StudentMessage(name,chinese,math,english)
                print(student)
        except Exception as e:
            print("添加失败!")
            print("请联系开发人员,错误为:",e)
    def edit_student(self):
        try:
            name = input("请输入要修改信息的学生姓名:")
            self.r_json()
            if name not in self.system:
                print(f"{name}没有在教务系统中,修改失败!")
            else:
                chinese = self.input_score("语文")
                math = self.input_score("数学")
                english = self.input_score("英语")
                self.system[name] = {
                    "姓名" : name,
                    "语文" : chinese,
                    "数学" : math,
                    "英语" : english,
                    "总分" : chinese + math + english
                }
                self.w_json()
                print(f"{name}的信息修改成功~")
                student = StudentMessage(name,chinese,math,english)
                print(student)
        except Exception as e:
            print("修改失败!")
            print("请联系开发人员,错误为:",e)
    def delete_student(self):
        try:
            name = input("请输入要删除的学生姓名:")
            self.r_json()
            if name not in self.system:
                print(f"{name}不在教务系统中,删除失败!")
            else:
                del self.system[name]
                self.w_json()
                print(f"{name}的信息删除成功~")
        except Exception as e:
            print("删除失败!")
            print("请联系开发人员,错误为:",e)
    def delete_all_students(self):
        try:
            self.system = {}
            self.w_json()
            print("全部删除成功~")
        except Exception as e:
            print("全部删除失败!")
            print("请联系开发人员,错误为:",e)
    def find_student(self):
        try:
            name = input("请输入要查询的学生姓名:")
            self.r_json()
            if name not in self.system:
                print(f"{name}不在教务系统中,查询失败!")
            else:
                print("查询成功~")
                student = StudentMessage(name,self.system[name]["语文"],self.system[name]["数学"],self.system[name]["英语"])
                print(student)
        except Exception as e:
            print("查询失败!")
            print("请联系开发人员,错误为:",e)
    def get_all_students(self):
        try:
            self.r_json()
            print("查询成功~")
            print("全部学生信息如下:")
            for name in self.system:
                student = StudentMessage(name,self.system[name]["语文"],self.system[name]["数学"],self.system[name]["英语"])
                print(student)
        except Exception as e:
            print("查询失败!")
            print("请联系开发人员,错误为:",e)
    def sort_students(self):
        try:
            list1 = []
            self.r_json()
            for name in self.system:
                list1.append(self.system[name])
            list1.sort(key=lambda item : item["总分"],reverse=True)
            print(list1)
            for i in list1:
                student = StudentMessage(i["姓名"], i["语文"], i["数学"], i["英语"])
                print(student)
        except Exception as e:
            print("查询失败!")
            print("请联系开发人员,错误为:", e)
student = EducationManagement()
while True:
    print("""
    ------------------------------------------------------------------------------------------------------------------------
    1.添加学生信息 | 2.修改学生信息 | 3.删除学生信息 | 4.删除全部学生信息 | 5.查询学生信息 | 6.查看全部学生信息 | 7.按成绩排序 | 8.退出教务系统
    ------------------------------------------------------------------------------------------------------------------------
    """)
    num = input("请输入功能编号(1-8):")
    match num:
        case "1":
            student.add_student()
        case "2":
            student.edit_student()
        case "3":
            student.delete_student()
        case "4":
            student.delete_all_students()
        case "5":
            student.find_student()
        case "6":
            student.get_all_students()
        case "7":
            student.sort_students()
        case "8":
            print("感谢使用本教务系统,byebye~~")
            break
        case _:
            print("操作错误,请重新选择功能编号(1-7)")