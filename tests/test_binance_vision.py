from quantbot.data.binance_vision import month_range, parse_klines_csv

MS_ROW = b"1700000000000,1,2,0.5,1.5,10,1700003599999,15,7,4,6,0\n"
US_ROW = b"1700000000000000,1,2,0.5,1.5,10,1700003599999999,15,7,4,6,0\n"


def test_month_range_inclusive():
    assert month_range("2025-11", "2026-02") == ["2025-11", "2025-12", "2026-01", "2026-02"]


def test_parse_handles_millisecond_and_microsecond_timestamps():
    a, b = parse_klines_csv(MS_ROW), parse_klines_csv(US_ROW)
    assert a.index[0] == b.index[0]
    assert str(a.index[0]) == "2023-11-14 22:13:20+00:00"
    assert list(a.columns) == ["open", "high", "low", "close", "volume", "quote_volume", "trades"]
    assert a["close"].iloc[0] == 1.5
