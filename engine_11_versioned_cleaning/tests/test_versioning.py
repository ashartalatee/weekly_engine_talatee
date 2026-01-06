def test_version_increment():
    from src.version_tracker import get_next_version_id

    versions = [
        {"version_id": 1},
        {"version_id": 2}
    ]
    assert get_next_version_id(versions) == 3
