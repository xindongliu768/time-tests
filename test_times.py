from times import compute_overlap_time, time_range


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    assert compute_overlap_time(large, short) == [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]


def test_no_overlap():
    range1 = time_range("2026-11-02 09:00:00", "2026-11-02 10:00:00")
    range2 = time_range("2026-11-02 11:00:00", "2026-11-02 12:00:00")

    assert compute_overlap_time(range1, range2) == []


def test_multiple_intervals():
    # Two one-hour intervals in each range, separated by a one-hour gap.
    range1 = time_range(
        "2026-11-02 09:00:00", "2026-11-02 12:00:00",
        number_of_intervals=2, gap_between_intervals_s=3600,
    )
    range2 = time_range(
        "2026-11-02 09:30:00", "2026-11-02 12:30:00",
        number_of_intervals=2, gap_between_intervals_s=3600,
    )

    assert compute_overlap_time(range1, range2) == [
        ("2026-11-02 09:30:00", "2026-11-02 10:00:00"),
        ("2026-11-02 11:30:00", "2026-11-02 12:00:00"),
    ]


def test_touching_intervals():
    # Sharing an endpoint does not give an overlap of positive duration.
    range1 = time_range("2026-11-02 09:00:00", "2026-11-02 10:00:00")
    range2 = time_range("2026-11-02 10:00:00", "2026-11-02 11:00:00")

    assert compute_overlap_time(range1, range2) == []
