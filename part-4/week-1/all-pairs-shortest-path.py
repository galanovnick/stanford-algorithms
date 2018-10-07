from utils.dataprovider import get


def parse(raw):
    lines = raw.split('\n')
    lines.pop(-1)
    meta = lines.pop(0)

    adj_list = list()

    index = -1
    for line in lines:
        [source, dest, weight] = line.split(' ')
        if int(source) != index:
            index = int(source)
            adj_list.append(list())

        adj_list[index - 1].append({"dest": dest, "weight": weight})

    return adj_list


def get_apsp(graph):
    n = len(graph)


def get_sp(graph):
    n = len(graph)


graph_raw = get('https://d3c33hcgiwev3.cloudfront.net/_6ff856efca965e8774eb18584754fd65_g1.txt?Expires=1539043200&Signatu'
            're=ZaTS5934vxjoCHePeMOt8NepyzXKi2BH8WreGzt0je0fWQIDnd0stmPH7NJCGWI7au-cq85ljlv7CiSvvifdu5sosL0HL4IqDiMl'
            'lDG3YPHJrYrzpnn5Rk~Lc5MSqX4hztlZw5dMmsyJSehLwdyUBQkL3jwaI9Wwkh~O9zwiE00_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A')

graph_data = parse(graph_raw)

