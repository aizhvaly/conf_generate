# -*- coding: utf-8 -*-


import ipaddress as ip


def envs(enviroment):
    """

    Принимает переменные для шаблона Jinja2:

        Данные приходят с формы /templates/index.html
        На выходе получает словаррь с переменными

    """
    def vlan_range(unit):

        """
        переменная со значениями
        section - имя переменной для записи в лог.
        Обрабатывает строки типа:
        1) 1,2,3,4
        2) 1-4
        3) 1-4,100-110
        Отдаст список с int в словарь enviroment

        """

        try:

            if ',' and not '-' in unit:
                unit = unit.replace(' ', '').split(',')
                for i in range(len(unit)):
                    unit[i] = int(unit[i])

            elif '-' and not ',' in unit:
                unit = unit.replace(' ', '').split('-')
                for i in range(int(unit[1]) - int(unit[0])):
                    i += 1
                    unit.append(int(unit[0]) + i)

                unit[0] = int(unit[0])
                unit.remove(unit[1])

            elif ',' and '-' in unit:
                unit = unit.replace(' ', '').split(',')
                for i in range(len(unit)):
                    if '-' in unit[i]:
                        RANGE_VLAN = unit[i].split('-')
                        unit.remove(unit[i])
                        unit.append(int(RANGE_VLAN[0]))
                        for i in range(int(RANGE_VLAN[1]) - int(RANGE_VLAN[0])):
                            i += 1
                            unit.append(int(RANGE_VLAN[0]) + i)
                    else:
                        unit[i] = int(unit[i])
                unit.sort()

        except ValueError or TypeError as err_msg:
            print(err_msg + '\nНеправильный ввод переменных')
#            with open(os.path.join(os.path.dirname(__file__)) + '/crash_log', 'a+') as f:
#                f.write(time.asctime() + '  :  section : ' + section)
#                f.write(str(err_msg) + '\n')
        return unit


    def net_details(net_details, hostname=enviroment[0]):
        """
        net_details ожидает на входит строку формата "ip/prefix"

            TODO: дописать проверку ip адреса через phpipam #Done in views.py

        На выходе в словарь enviroment добавляется словарь net_details c полями:
        examples:
        net_details_ip_prefix = 10.10.1.10/24
        net_details_net = 10.10.1.0/24
        net_details_ip = 10.10.1.10
        net_details_ip_with_netmask = 10.10.1.10/255.255.255.0
        net_details_netmask = 255.255.255.0
        net_details_reverse_mask = 0.0.0.255
        net_details_arpa = 10.1.10.10.in-addr.arpa
        net_details_arpa_for_bind = 10.1.10.10.in-addr.arpa. IN PTR sw1
        net_details_def_gateway = 10.10.1.1

        """
        net_details = ip.ip_interface(net_details)
        net_details_ip_prefix = net_details.compressed
        net_details_net = net_details.network.compressed
        net_details_ip = net_details.ip.compressed
        net_details_ip_with_netmask = net_details.with_netmask
        net_details_netmask = net_details.netmask.compressed
        net_details_reverse_mask = net_details.hostmask.compressed
        net_details_arpa = net_details.ip.reverse_pointer
        net_details_ptr = net_details.ip.reverse_pointer + '. IN PTR ' + hostname
        net_details_def_gateway = list(net_details.network.hosts())[0].compressed

        net_details = {'net_details_ip_prefix': net_details_ip_prefix,\
                       'net_details_net': net_details_net,\
                       'net_details_ip': net_details_ip,\
                       'net_details_ip_with_netmask': net_details_ip_with_netmask,\
                       'net_details_netmask': net_details_netmask,\
                       'net_details_reverse_mask': net_details_reverse_mask,\
                       'net_details_arpa': net_details_arpa,\
                       'net_details_ptr': net_details_ptr,\
                       'net_details_def_gateway': net_details_def_gateway
                       }
        return net_details

    #TODO: mstp_id, dhcp_relay vlan_id, snmp community % string, igmp_snnoop vlan

    enviroment = {'hostname' : enviroment[0], 'mgmt_vlan' : vlan_range(enviroment[1]), 'user_vlan' : vlan_range(enviroment[2]),\
                'other_user_vlans' : vlan_range(enviroment[3]),\
                'net_details' : net_details(enviroment[4]), 'path': enviroment[5]}
    return enviroment

def main():
    pass
if __name__  == '__main__':
    main()
