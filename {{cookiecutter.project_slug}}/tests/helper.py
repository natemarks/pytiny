"""helper functions for test modules

"""
import os



class Golden:
    """golden file helper class

    """
    def __init__(self, request) -> None:
        self.update_golden = request.config.getoption("--update_golden")
        self.test_module_path = request.fspath
        self.test_module_dir = os.path.dirname(self.test_module_path)
        self.test_name = request.node.name
        self.test_case = request.node.originalname if hasattr(
            request.node, 'originalname') else ''

        self.data_dir = os.path.join(self.test_module_dir, "data")

        self.file_path = os.path.join(
            self.data_dir,
            f"{self.test_name}_{self.test_case}_golden.txt")
        
    def update(self, actual_data):
        """update golden file with actual data

        Args:
            actual_data (str): actual data to be written to golden file
        """
        if not self.update_golden:
            return
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        with open(self.file_path, "w", encoding="utf-8") as golden_file:
            golden_file.write(actual_data)

    def expected(self)->str:
        """read golden file and return its contents

        Returns:
            str: contents of golden file
        """
        with open(self.file_path, "r", encoding="utf-8") as golden_file:
            return golden_file.read()
