Desafio QA – Coco Bambu

Objetivo
Automatizar testes de UI e API relacionados ao fluxo de compra no site

Tecnologias
- Python 3
- Selenium
- requests
- pytest

Estrutura
- `tests/test_add_to_cart.py`: teste de UI com Selenium
- `tests/test_cart_api.py`: testes de API (add, update, delete)

Executando localmente

````bash
pip install -r requirements.txt
pytest
