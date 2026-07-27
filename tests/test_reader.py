from src.reader import read_csv

def test_read_csv():
    df = read_csv("data/Ober-Eschbach_W15min.csv")

    assert not df.empty