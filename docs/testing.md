# Testing Guide

## Test Types

### 1. Unit Tests
- Test individual components
- Mock dependencies
- Fast execution

### 2. Integration Tests
- Test component interactions
- Use real dependencies
- End-to-end scenarios

### 3. Performance Tests
- Load testing
- Stress testing
- Benchmarking

## Writing Tests

### Unit Test Example
```python
from odoo.tests.common import TransactionCase

class TestProduct(TransactionCase):
    def setUp(self):
        super().setUp()
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'product',
        })

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
```

### Integration Test Example
```python
from odoo.tests.common import HttpCase

class TestWebsite(HttpCase):
    def test_shop_page(self):
        self.start_tour('/shop', 'shop_buy_product')
```

## Test Coverage

1. Run tests with coverage:
```bash
coverage run odoo-bin -c odoo.conf -d test_db --test-enable --stop-after-init
```

2. Generate coverage report:
```bash
coverage report
coverage html
```

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Run Tests
        run: |
          pip install -r requirements.txt
          python -m pytest
```