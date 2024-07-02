import datetime
import unittest
import os

def log_message(file_name, message, level):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{date}] [{level}] {message}\n"
    with open(file_name, "a") as file:
        file.write(entry)

class TestLogMessage(unittest.TestCase):

    def setUp(self):

        self.file_name = "test_application.log"
        with open(self.file_name, "w") as file:
            file.write("")

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_log_info_message(self):
        log_message(self.file_name, "User logged in", "INFO")
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            
        self.assertEqual(len(lines), 1)
        self.assertIn("[INFO] User logged in", lines[0])

    def test_log_warning_message(self):
        log_message(self.file_name, "Failed login attempt", "WARNING")
        with open(self.file_name, "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 1)
        self.assertIn("[WARNING] Failed login attempt", lines[0])

    def test_log_error_message(self):
        log_message(self.file_name, "Application error 500 Code", "ERROR")
        with open(self.file_name, "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 1)
        self.assertIn("[ERROR] Application error 500 Code", lines[0])

    def test_log_multiple_messages(self):
        log_message(self.file_name, "User logged in", "INFO")
        log_message(self.file_name, "Failed login attempt", "WARNING")
        log_message(self.file_name, "Application error 500 Code", "ERROR")
        with open(self.file_name, "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 3)
        self.assertIn("[INFO] User logged in", lines[0])
        self.assertIn("[WARNING] Failed login attempt", lines[1])
        self.assertIn("[ERROR] Application error 500 Code", lines[2])

if __name__ == "__main__":
    unittest.main()

#Sites where research was carried out for completion.

#https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python
#https://stackoverflow.com/questions/7588511/format-a-datetime-into-a-string-with-milliseconds
#https://www.analyticsvidhya.com/blog/2024/01/all-about-python-strftime-function/