from django.shortcuts import render
from django.http import *
from config_generator.pyapp.envs import envs
from config_generator.pyapp.temps_generate import temps_generate
from config_generator.pyapp.phpipam import PhpIpAm


def index_main(request):

    return render(request, 'index.html')


def config_generator(request):

    if request.method == "GET":
        enviroment = [request.GET['hostname'], request.GET['mgmt_vlan'], request.GET['user_vlan'],\
                    request.GET['other_user_vlans'], request.GET['net_details_s'], request.GET['path']]
        data = envs(enviroment)
        check_ipam = PhpIpAm()
        if check_ipam._mode == 'on':
            result = check_ipam.check_ip(data['net_details']['net_details_net'], data['net_details']['net_details_ip'])
            if result == 'Clear':
                res = temps_generate(data)
                return HttpResponse(res)
            else:
                return HttpResponse(result)
        else:
            res = temps_generate(data)
            return HttpResponse(res)



