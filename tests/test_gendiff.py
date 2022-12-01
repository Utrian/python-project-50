from pytest import fixture
from gendiff.gendiff_with_formatter import generate_diff
import gendiff.formatters.stylish as ft_stylish
import gendiff.formatters.plain as ft_plain
import gendiff.formatters.json as ft_json


@fixture
def json_first_file():
    return 'tests/fixtures/json/first_file.json'


@fixture
def json_second_file():
    return 'tests/fixtures/json/second_file.json'


@fixture
def yaml_first_file():
    return 'tests/fixtures/yaml/first_file.yaml'


@fixture
def yaml_second_file():
    return 'tests/fixtures/yaml/second_file.yaml'


# @fixture
# def path_output_test_file():
#     return 'tests/output.txt'


# @fixture
# def result_output():
#     with open('tests/output.txt') as f:
#         return f.read()


# @fixture
# def unformatted_diff():
#     with open('tests/fixtures/output/unformatted_diff.txt') as f:
#         return f.read()


@fixture
def stylish_formatted_diff():
    with open('tests/fixtures/output/stylish_formatted_diff.txt') as f:
        return f.read()


@fixture
def plain_formatted_diff():
    with open('tests/fixtures/output/plain_formatted_diff.txt') as f:
        return f.read()


# @fixture
# def json_formatted_diff():
#     with open('tests/fixtures/output/json_formatted_diff.txt') as f:
#         return f.read()


# def test_generate_diff_json(
#                         json_first_file,
#                         json_second_file,
#                         unformatted_diff
# ):
#     unformatted_diff_json = gendiff.generate_diff(
#         json_first_file, json_second_file
#     )

#     assert str(unformatted_diff_json) == unformatted_diff


# def test_generate_diff_jaml(
#                         yaml_first_file,
#                         yaml_second_file,
#                         unformatted_diff
# ):
#     unformatted_diff_yaml = gendiff.generate_diff(
#         yaml_first_file, yaml_second_file
#     )

#     assert str(unformatted_diff_yaml) == unformatted_diff


def test_stylish_json(
                        json_first_file,
                        json_second_file,
                        stylish_formatted_diff
):
    result_formatted_diff = generate_diff(
                                        json_first_file,
                                        json_second_file,
                                        ft_stylish.stylish
    )

    assert result_formatted_diff == stylish_formatted_diff


def test_stylish_yaml(
                        yaml_first_file,
                        yaml_second_file,
                        stylish_formatted_diff
):
    result_formatted_diff = generate_diff(
                                        yaml_first_file,
                                        yaml_second_file,
                                        ft_stylish.stylish
    )

    assert result_formatted_diff == stylish_formatted_diff


def test_plain_json(
                    json_first_file,
                    json_second_file,
                    plain_formatted_diff
):
    result_formatted_diff = generate_diff(
                                        json_first_file,
                                        json_second_file,
                                        ft_plain.plain
    )

    assert result_formatted_diff == plain_formatted_diff


def test_plain_yaml(
                    yaml_first_file,
                    yaml_second_file,
                    plain_formatted_diff
):
    result_formatted_diff = generate_diff(
                                        yaml_first_file,
                                        yaml_second_file,
                                        ft_plain.plain
    )

    assert result_formatted_diff == plain_formatted_diff


# def test_diff_to_json_with_json_file(
#                                     json_first_file,
#                                     json_second_file,
#                                     json_formatted_diff
# ):
#     formatted_diff_json = gendiff_with_formatter.generate_diff(
#         json_first_file, json_second_file, ft_json.diff_to_json
#     )

#     assert formatted_diff_json == json_formatted_diff


# def test_diff_to_json_with_yaml_file(
#                                     yaml_first_file,
#                                     yaml_second_file,
#                                     json_formatted_diff
# ):
#     formatted_diff_yaml = gendiff_with_formatter.generate_diff(
#         yaml_first_file, yaml_second_file, ft_json.diff_to_json
#     )

#     assert formatted_diff_yaml == json_formatted_diff
