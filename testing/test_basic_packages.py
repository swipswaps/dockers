def test_pandas_excel():
    import pandas as pd

    # TODO: actually get correct path
    xl = pd.ExcelFile(
        'test_excel_workbook.xlsx'
    )
    df = xl.parse()
    df2 = pd.read_excel(
        'test_excel_workbook.xlsx'
    )
    assert df.shape == df2.shape


def test_pandas_read_csv():
    import pandas as pd
    # TODO: actually get correct path
    df = pd.read_csv(
        'test_csv.csv'  # noqa: E501
    )
    assert df.shape == (1, 6)

# TODO: new path or query


def test_matplotlib():
    import matplotlib.pyplot as plt
    import numpy as np

    # TODO: convert to using mock data

    x = np.arange(0.5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)


def test_numpy():
    import numpy as np

    x = np.random.choice(np.random.sample(100), 10)
    assert len(x) == 10


def test_scipy():
    from scipy.special import comb

    com = comb(100, 10, exact=False, repetition=True)
    assert com == 42634215112709.99


def get_inverse(x):
    return 1 / x


def test_multiprocessing():
    from multiprocessing import Pool

    p = Pool(5)
    results = p.map(get_inverse, range(2, 8))
    assert results == [
        0.5,
        0.3333333333333333,
        0.25,
        0.2,
        0.16666666666666666,
        0.14285714285714285,
    ]


def test_itertools():
    from itertools import product

    x = list(product([1, 2, 3], repeat=2))
    assert len(x) == 9


def test_re():
    import re

    x = re.split(r'\W+', 'Words, words, words.')
    assert len(x) == 4


def test_pickle():
    import pickle
    import os

    favorite_color = 'blue'
    with open('save.p', 'wb') as f:
        pickle.dump(favorite_color, f)
    with open('save.p', 'rb') as f:
        favorite_color_2 = pickle.load(f)
    os.remove('save.p')
    assert favorite_color == favorite_color_2


def test_contextily():
    from pyproj import Proj
    import contextily as ctx

    proj = Proj('+init=epsg:3857')

    assert proj
    assert ctx.sources.ST_TONER == 'http://tile.stamen.com/toner/tileZ/tileX/tileY.png'  # noqa: E501


def test_requests():
    import requests
    get = requests.get('https://www.google.com')
    assert get.status_code == 200


def test_camelot():
    import camelot
    tables = camelot.read_pdf('test_pdf.pdf')
    assert tables[0].shape == (7, 7)


def test_jupyter():
    import subprocess
    import requests
    # start jupyter lab, don't wait for it to return
    process = subprocess.Popen(args=['jupyter', 'lab'], stdin=None,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
    # get contents of lsof based on pid, will obtain port process
    # is listening on
    lsof = subprocess.Popen(
        ['lsof', '-i', '-a', '-p', str(process.pid)], stdout=subprocess.PIPE)
    # get output of lsof command
    lsof_output, _ = lsof.communicate()
    # remove header and pull out hostname
    host_line = lsof_output.decode('utf-8').split('\n')[1]
    host = host_line.split()[8]
    # attempt to connect to host, test if 200 response code is obtained
    get = requests.get('http://' + host)
    # close processes
    process.terminate()
    lsof.terminate()
    assert get.status_code == 200

def test_tabula():
    import tabula
    df = tabula.read_pdf('test_pdf.pdf', pages='1')
    assert df[0].shape == (8, 6)

# TODO: boto3, dask
