from os import listdir

from config.system import Characters


def get_files_names_list(
    *,
    extenstion: str,
    folder_path: str,
) -> list[str]:

    files_names_list: list[str] = []
    folder: list[str] = listdir(folder_path)

    for file_name in folder:
        file_ending: str = Characters.DOT.value + extenstion
        file_has_given_extension: bool = file_name.endswith(file_ending)

        if file_has_given_extension:
            files_names_list.append(file_name)

    return files_names_list


def get_dictionaries_list_from_strings_list(
    *,
    strings_list: list[str],
    split_character: str = Characters.MINUS.value,
) -> list[dict]:

    dictionaries_list: list[dict] = []

    for file_name in strings_list:
        dictionary: dict = {}

        tokens_list: list[str] = file_name.split(split_character)

        keys_list: list[str] = []
        values_list: list[str] = []

        for index, token in enumerate(tokens_list):
            token_is_key: bool = index % 2 == 0
            token_is_value: bool = index % 2 == 1

            list_map: dict[bool, list[str]] = {
                token_is_key: keys_list,
                token_is_value: values_list,
            }

            result_list: list[str] = list_map[True]
            result_list.append(token)

        keys_list_length: int = len(keys_list)
        values_list_length: int = len(values_list)

        extra_key_exists: bool = keys_list_length > values_list_length

        if extra_key_exists:
            keys_list.pop()

        for index in range(values_list_length):
            key: str = keys_list[index]
            value: str = values_list[index]

            dictionary[key] = value

        dictionaries_list.append(dictionary)

    return dictionaries_list


def do_lists_have_same_length(
    *,
    lists_matrix: list[list],
) -> bool:

    lists_matrix_is_empty: bool = not lists_matrix

    if lists_matrix_is_empty:
        return False

    first_list: list = lists_matrix[0]
    etalon_length: int = len(first_list)

    for list_object in lists_matrix[1:]:
        list_object_length: int = len(list_object)
        lengths_mismatch_happened: bool = list_object_length != etalon_length

        if lengths_mismatch_happened:
            return False

    return True
