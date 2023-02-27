from project_code.example_code import get_hello_world


# [Optional] Use classes to group test functions
class TestHelloWorld:
    # Pytest tests are defined as functions
    # Names must start with "test_" to be discovered by pytest
    def test_return(self):
        # Try to follow this schema: got vs expected
        got = get_hello_world()
        expected = "Hello World!"

        # Use pytest's assert statement(s) for checks.
        # It makes sure to run all tests even if one fails.
        assert got == expected

        # Example of a failing test - uncomment next line to see the effect
        # assert got == 3
