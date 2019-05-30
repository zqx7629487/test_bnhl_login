from Base.get_file_data import data
import os, sys


# sys.path.append(os.getcwd())
class TestTabOne:

    # 读取yaml数据
    def est_login(self):

        # 预期成功列表
        suc_list = []
        # 预期失败列表
        fail_list = []

        data_list = data("login.yaml")
        for i in data_list.values():
            if i.get("toast"):
                fail_list.append((i.get("account"), i.get("passwd"),
                                  i.get("toast"), i.get("expect_data")))
            else:
                suc_list.append((i.get("account"), i.get("passwd"),
                                 i.get("expect_data")))
        data_dict = {"suc": suc_list, "fail": fail_list}
        print(data_dict)
        return data_dict


get_data = TestTabOne()
txt = get_data.est_login().get("suc")
print(txt)




