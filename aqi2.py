# -*- coding:utf-8 -*-

import json


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w')
    json.dump(top5_list, f)
    f.close()

if __name__ == '__main__':
    main()