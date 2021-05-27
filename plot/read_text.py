import matplotlib.pyplot as plt
from datetime import datetime
import sys


def open_file(file='data.txt'):
    ouf = open(file)
    data = ouf.readlines()
    ouf.close()
    return data


def sort_by_date(data):
    headers = data.pop(0).strip(' ').strip('\n').split(', ')
    # info = []
    # for elem in data:
    #     info.append(dict(zip(headers, elem.strip().split(','))))
    info = [dict(zip(headers, elem.strip().split(','))) for elem in data]
    for elem in info:
        elem['resource'] = int(elem['resource'])
        elem['count'] = int(elem['count'])
        elem['date'] = datetime.strptime(elem['date'], '%Y-%m').date()
    sorted_info = sorted(info, key=lambda x: x['date'])
    return sorted_info


def sort_by_resource(sorted_info):
    resources = []
    for elem in sorted_info:
        resources.append(elem['resource'])
    resources.sort()
    unique_resources = list(set(resources))
    res_by_list = []
    for i in unique_resources:
        res_by_list.append(list(filter(lambda elem: elem['resource'] == i, sorted_info)))
    return res_by_list


def create_plot(res_by_list, staff_key, resource_key):
    abscissa = []
    ordinate = []
    staff = staff_key
    num_of_resource = resource_key
    if staff != 'None':
        for elem in res_by_list:
            for dc in elem:
                    if dc['staff_id'] == staff and dc['resource'] == num_of_resource:
                        abscissa.append(dc['date'])
                        ordinate.append(dc['count'])
    else:
        for elem in res_by_list:
            for dc in elem:
                    if dc['resource'] == num_of_resource:
                        abscissa.append(dc['date'])
                        ordinate.append(dc['count'])
    if staff != 'None':
        plt.title(staff)
    else:
        plt.title(num_of_resource)
    plt.xlabel('date')
    plt.ylabel('count')
    plt.plot(abscissa, ordinate, 'o')
    plt.show()


def main(file):
    data_str = open_file(file)
    if data_str == 'date, resource, count, staff_id':
        break
    sorted_info = sort_by_date(data_str)
    res_by_list = sort_by_resource(sorted_info)
    create_plot(res_by_list, sys.argv[1], int(sys.argv[2]))

#if you want info without staff, type 'None', 'number of resource'
#if you want info with staff, type 'Name of staff', 'number of resource'

if __name__ == '__main__':
    main('data.txt')
