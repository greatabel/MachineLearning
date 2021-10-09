import codecs


def read_voca_file(file_path):
    """
    Read vocabulary file
    :param file_path: The path of vocabulary file
    :return: vocabulary list
    """
    vocas = list()

    with codecs.open(file_path, "r", "utf-8") as voca_file:
        for each_line in voca_file:
            result = "".join([i for i in each_line if not i.isdigit()])
            result = result.strip()
            vocas.append(result)

    return vocas
