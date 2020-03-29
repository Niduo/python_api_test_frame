# coding = utf-8
import json


def is_json(my_json):
    """
    判断是否是一个json格式数据
    :param my_json: 传入参数
    :return: 布尔值
    """
    try:
        json.load(my_json)
        print('是一个json')
        return True

    except Exception as e:
        return False
        print('不是一个合法的json格式！', e)

    # finally:
    #     return False





