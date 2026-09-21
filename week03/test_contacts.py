import unittest
from contacts_class import Contact, PersonalContact, BusinessContact


class TestContact(unittest.TestCase):
    def test_create_contact(self):
        c = Contact("小明", "13800000000")
        self.assertEqual(c.name, "小明")
        self.assertEqual(c.phone, "13800000000")

    def test_to_dict(self):
        c = Contact("小明", "13800000000")
        d = c.to_dict()
        self.assertEqual(d["name"], "小明")
        self.assertEqual(d["type"], "contact")

    def test_from_dict(self):
        d = {"type": "contact", "name": "小明", "phone": "13800000000"}
        c = Contact.from_dict(d)
        self.assertEqual(c.name, "小明")
        self.assertIsInstance(c, Contact)

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            Contact("小明", "不是电话")


class TestPersonalContact(unittest.TestCase):
    def test_create(self):
        c = PersonalContact("小明", "13800000000", "2000-01-01", "朋友")
        self.assertEqual(c.birthday, "2000-01-01")
        self.assertEqual(c.relation, "朋友")

    def test_to_dict_has_extra_fields(self):
        c = PersonalContact("小明", "13800000000", "2000-01-01", "朋友")
        d = c.to_dict()
        self.assertEqual(d["type"], "personal")
        self.assertEqual(d["birthday"], "2000-01-01")
        self.assertEqual(d["relation"], "朋友")


class TestBusinessContact(unittest.TestCase):
    def test_create(self):
        c = BusinessContact("李总", "13900000000", "某公司", "经理")
        self.assertEqual(c.company, "某公司")
        self.assertEqual(c.title, "经理")

    def test_to_dict_has_extra_fields(self):
        c = BusinessContact("李总", "13900000000", "某公司", "经理")
        d = c.to_dict()
        self.assertEqual(d["type"], "business")
        self.assertEqual(d["company"], "某公司")


if __name__ == "__main__":
    unittest.main()
