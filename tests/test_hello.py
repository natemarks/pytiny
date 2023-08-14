"""test the hello module using golden files
"""

import pytest
from tests.helper import Golden
from {{cookiecutter.project_slug}}.hello import hello


@pytest.mark.unit
@pytest.mark.parametrize(
    "",
    [
        pytest.param(id="sandbox"),
        pytest.param(id="dev"),
        pytest.param(id="production"),
    ],
)
def test_environment(request):
    """test Environment loading some simple data

    This test covers Environment with a FlatStore as input


    """
    result = hello(request.node.originalname)
    golden = Golden(request)
    golden.update(result)
    assert result == golden.expected()
