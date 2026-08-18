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
