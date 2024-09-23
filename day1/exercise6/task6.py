import json
from typing import Union, List, Dict


def merge_sorted_movie_lists(file_path: str) -> Union[str, str]:
    try:
        with open(file_path, 'r') as file:
            data: Dict[str, List[Dict[str, Union[str, int]]]] = json.load(file)

            if not isinstance(data, dict) or 'list1' not in data or \
                    'list2' not in data:
                return "Invalid data"

            list1: List[Dict[str, Union[str, int]]] = data['list1']
            list2: List[Dict[str, Union[str, int]]] = data['list2']

            if not all(isinstance(item, dict) and 'title' in item and
                       'year' in item for item in list1 + list2):
                return "Invalid data"

            merged_list: List[Dict[str, Union[str, int]]] = sorted(
                list1 + list2, key=lambda x: x['year'])

            return json.dumps({"list0": merged_list})
    except (json.JSONDecodeError, IOError):
        return "Invalid format"


def main() -> None:
    print(merge_sorted_movie_lists("input.txt"))


if __name__ == "__main__":
    main()
