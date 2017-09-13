#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
Just test
'''


EXAMPLES = '''
Get the name
- name: Test that my module works
  swapi:
    area: "people"
    id: 1
    field: "name"
  register: result

'''

from ansible.module_utils.basic import *
import requests

def main():
    url = 'https://swapi.co/api'
    fields = {
        "area" : {"required": True, "type": "str" },
        "id": {"required": True, "type": "int" },
        "field": {"required": False, "type": "str" }
    }

    module = AnsibleModule(argument_spec = fields, supports_check_mode = False)

    area = module.params['area']
    id = module.params['id']
    field = module.params['field']

    request_url = url + '/' + area + '/' + str(id)
    result = requests.get(request_url)
    data = result.json()
    ret = data[field]

    module.exit_json(changed=False, meta=ret)


if __name__ == '__main__':
    main()
