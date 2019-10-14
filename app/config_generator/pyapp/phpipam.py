import json
import requests
import os
import sys


class PhpIpAm(object):

    def __init__(self, cfg_file='config.json'):

        self._verify = False
        self._token = None
        self._url = None
        self._user = None
        self._passwd = None
        self._auth_url = None
        self._mode = None
        self.load_config(cfg_file)
        if self._mode == "on":
            self.auth_session()
        else:
            pass


    def load_config(self, cfg_file='config.json'):
        with open(cfg_file) as json_file:
            data = json.load(json_file)
            self._url = data['api_url']
            self._user = data['user']
            self._passwd = data['passwd']
            self._mode = data['mode']
            self._auth_url = data['api_url'] + 'user/'

    def auth_session(self):
        """
        Authenticate on PHPIPAM API
        """
        req = requests.post(self._auth_url, auth=(self._user, self._passwd),
                            verify=self._verify)
        if req.status_code != 200:
            raise requests.exceptions.RequestException(
                "Authentication failed on {0}".format(self._auth_url))
        self._token = {"token": req.json()['data']['token']}
        return req

    def check_ip(self, subnet, ip):
        url_net = self._url + 'subnets/cidr/{subnet}'.format(subnet=subnet)
        req_subnet = requests.get(url_net, headers=self._token, verify=self._verify)
        if req_subnet.json()['success'] == False:
            return req_subnet.json()["message"]
        else:
            sectionID = req_subnet.json()['data'][0]['sectionId']
            subnetID = req_subnet.json()['data'][0]['id']
            url_ip = self._url + 'addresses/{ip}/{subnetID}'.format(ip=ip, subnetID=subnetID)
            req_ip = requests.get(url_ip, headers=self._token, verify=self._verify)
            if req_ip.json()['success'] == False:
                return "Clear"
            else:
                ipID = req_ip.json()['data']['id']
                link = 'http://10.35.131.136:10199/phpipam/index.php?page=subnets&section={sectionID}&subnetId={subnetID}&sPage=address-details&ipaddrid={ipID}'.format(sectionID=sectionID,\
                                                                                                                                                       subnetID=subnetID, ipID=ipID)
                return link
