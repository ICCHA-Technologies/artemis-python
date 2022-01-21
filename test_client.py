import client
import service
import unittest

class TestClient(unittest.TestCase):
    def test_client(self):
        print("\nStart client test...\n")

        test_service = service.Services()
        test_client = client.ClientStomp('/queue/channel','test message')
        # self.assertEqual(1+2,3,"El resultado es correcto")
        self.assertIsInstance(test_service,(service,), "Is an Instance")

if __name__ == '__main__':
    unittest.main()