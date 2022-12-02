import copy
import re


def find_unclosed_tags(path_to_html):
    with open(path_to_html, encoding='utf-8') as file:
        src = file.read()

    tags = re.findall(r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>", src)[1:]

    open_tags = [tag for tag in tags if '/' not in tag]
    close_tags = [tag for tag in tags if '/' in tag]

    open_tags_for_remove = copy.copy(open_tags)
    close_tags_for_remove = copy.copy(close_tags)

    result_open = [tag for tag in open_tags if
                   tag[:1] + '/' + tag[1:] not in close_tags_for_remove or close_tags_for_remove.remove(
                       tag[:1] + '/' + tag[1:])]
    result_close = [tag for tag in close_tags if
                    tag[:1] + tag[2:] not in open_tags_for_remove or open_tags_for_remove.remove(tag[:1] + tag[2:])]

    result = result_open + result_close

    return result



print(find_unclosed_tags('index.html'))
