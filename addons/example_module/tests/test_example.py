from odoo.tests.common import TransactionCase

class TestExample(TransactionCase):
    def setUp(self):
        super(TestExample, self).setUp()
        self.Example = self.env['example.model']

    def test_create_example(self):
        """Test example record creation"""
        example = self.Example.create({
            'name': 'Test Example',
            'description': 'Test Description',
        })
        self.assertEqual(example.name, 'Test Example')
        self.assertEqual(example.description, 'Test Description')

    def test_example_active(self):
        """Test example record active field"""
        example = self.Example.create({
            'name': 'Test Active',
        })
        self.assertTrue(example.active)
        example.active = False
        self.assertFalse(example.active)