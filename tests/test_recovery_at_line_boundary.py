import io
from typing import Union

import jsonlines
import pytest


@pytest.mark.parametrize("binary", [False, True])
def test_skip_invalid_preserves_next_line_at_boundary(binary: bool) -> None:
    stream: Union[io.BytesIO, io.StringIO]
    if binary:
        stream = io.BytesIO(b"bad\n4\n")
    else:
        stream = io.StringIO("bad\n4\n")

    with stream:
        with jsonlines.Reader(stream, max_line_length=3) as reader:
            observed = list(reader.iter(skip_invalid=True))
            assert observed == [4]
