import os
import unittest
import subprocess

class TestCheckScript(unittest.TestCase):
    def test_execucao_padrao(self):
        resultado = subprocess.run(["python3", "check.py"], capture_output=True, text=True)
        self.assertIn("Enviando log para API", resultado.stdout or resultado.stderr)

if __name__ == '__main__':
    unittest.main()
