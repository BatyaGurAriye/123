import subprocess
import unittest

class TestLinting(unittest.TestCase):
    def test_ruff(self):
        """Test that ruff linting passes without errors."""
        result = subprocess.run(['ruff', 'check', '.'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, msg=f'Ruff linting failed:\n{result.stdout}\n{result.stderr}')

if __name__ == '__main__':
    unittest.main()
