# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import properties
import unittest

from six import string_types

from .. import BaseModel
from ..exceptions import CannabisReportsValidationException


class TestModel(BaseModel):
    a_key = properties.String('A key')
    sub_instance = properties.Instance(
        'Sub Instance', instance_class=BaseModel,
    )
    list = properties.List(
        'List', prop=properties.Instance('List Instance',
                                         instance_class=BaseModel),
    )
    list_string = properties.List(
        'List of Strings', prop=properties.String('String'),
    )
    not_a_field = True


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        super(TestBaseModel, self).setUp()
        self.test_values = {
            'aKey': 'value',
            'subInstance': {
                'ucpc': '1234',
            },
            'list': [
                {'ucpc': '4321'},
            ],
        }
        self.internal_values = {
            'a_key': self.test_values['aKey'],
            'sub_instance': self.test_values['subInstance'],
            'list': self.test_values['list'],
        }

    def new_record(self):
        return TestModel.from_api(**self.test_values)

    def test_from_api_new_instance(self):
        """It should return a new instance of the class."""
        self.assertIsInstance(self.new_record(), TestModel)

    def test_from_api_camel_to_snake(self):
        """It should call the init with snake cased keys."""
        self.assertEqual(self.new_record().a_key, self.test_values['aKey'])

    def test_from_api_sub_instance(self):
        """It should properly instantiate sub-instances."""
        self.assertIsInstance(self.new_record().sub_instance, BaseModel)

    def test_from_api_list(self):
        """It should properly convert lists of instances."""
        res = self.new_record()
        self.assertIsInstance(res.list, list)
        self.assertIsInstance(res.list[0], BaseModel)

    def test_from_api_invalid_attribute(self):
        """It should remove any invalid attributes."""
        record = TestModel.from_api(**{'no_exist': 'value'})
        with self.assertRaises(AttributeError):
            record.no_exist

    def test_to_api_camel_case(self):
        """It should properly camel case the API args."""
        res = self.new_record().to_api()
        self.assertEqual(res['aKey'], self.internal_values['a_key'])

    def test_to_api_instance(self):
        """It should properly convert sub-instances to dict."""
        res = self.new_record().to_api()
        self.assertIsInstance(res['subInstance'], dict)

    def test_to_api_list(self):
        """It should properly convert sub-instances within lists props."""
        res = self.new_record().to_api()
        self.assertIsInstance(res['list'], list)
        self.assertIsInstance(res['list'][0], dict)

    def test_to_api_list_string(self):
        """It should properly handle naive lists."""
        expect = ['1', '2']
        self.test_values['list_string'] = expect
        res = self.new_record().to_api()
        self.assertIsInstance(res['listString'], list)
        self.assertIsInstance(res['listString'][0], string_types)

    def test_get_non_empty_vals(self):
        """It should return the dict without None and False."""
        expect = {
            'good_int': 1234,
            'bad_false': False,
            'good_true': True,
            'bad_none': None,
        }
        res = BaseModel.get_non_empty_vals(expect)
        del expect['bad_none'], expect['bad_false']
        self.assertDictEqual(res, expect)

    def test_parse_property_invalid_property(self):
        """It should raise an exception if property name is invalid."""
        with self.assertRaises(CannabisReportsValidationException):
            BaseModel._parse_property('no exist', 'value')

    def test_dict_lookup_exist(self):
        """It should return the attribute value when it exists."""
        self.assertEqual(
            self.new_record()['a_key'], self.internal_values['a_key'],
        )

    def test_dict_lookup_no_exist(self):
        """It should raise a KeyError when the attribute isn't a field."""
        with self.assertRaises(KeyError):
            self.new_record()['not_a_field']

    def test_dict_set_exist(self):
        """It should set the attribute via the items."""
        expect = 'Test-Expect'
        record = self.new_record()
        record['a_key'] = expect
        self.assertEqual(record.a_key, expect)

    def test_dict_set_no_exist(self):
        """It should raise a KeyError and not change the non-field."""
        record = self.new_record()
        with self.assertRaises(KeyError):
            record['not_a_field'] = False
        self.assertTrue(record.not_a_field)

    def test_get_exist(self):
        """It should return the attribute if it exists."""
        self.assertEqual(
            self.new_record().get('a_key'), self.internal_values['a_key'],
        )

    def test_get_no_exist(self):
        """It should return the default if the attribute doesn't exist."""
        expect = 'Test'
        self.assertEqual(
            self.new_record().get('not_a_field', expect), expect,
        )

    def test_from_api_list_no_model(self):
        """Test ``from_api`` when there is a list of non-property objects."""
        self.test_values['list_string'] = [
            'test', 'again',
        ]
        self.assertEqual(self.new_record().list_string,
                         self.test_values['list_string'])
